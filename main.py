from fileinput import filename
from pkgutil import iter_modules
from queue import Empty
import sys
import os
import io

from flask import Flask, flash, redirect, request, render_template
from google.cloud import storage
from google.cloud import vision

app = Flask(__name__, template_folder='template')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cloud-work-shop-36f89627d5a8.json"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Data Received")
    return render_template('index.html')


@app.route('/visionApi', methods=['GET', 'POST'])
def visionApi():

    image_uri = 'gs://cloud_work_shop/cloudTestImg.jpg'

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri

    response = client.label_detection(image=image)

    print('Labels (and confidence score):')
    # print('=' * 30)

    labels = response.label_annotations
    labelName = []
    labelScore = []

    for label in labels:
        resultV = label.description
        labelName.append(resultV)
        resultS = '%.2f%%' % (label.score*100.)
        labelScore.append(resultS)

    return render_template('label-detection.html', labelName=labelName, labelScore=labelScore)


@app.route('/object-detection', methods=['GET', 'POST'])
def objectDetection():

    image_uri = 'gs://cloud_work_shop/cloudTestImg.jpg'

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = image_uri

    response = client.object_localization(image=image)

    objects = response.localized_object_annotations
    objectName = []
    objectScore = []

    for obj in objects:
        resultN = obj.name
        objectName.append(resultN)
        resultS = '%.2f%%' % (obj.score*100.)
        objectScore.append(resultS)

    return render_template('label-detection.html', labelName=objectName, labelScore=objectScore)


@app.route('/callCatDog', methods=['GET', 'POST'])
def callCatDog():

    catImg = []
    dogImg = []

    bucket_name = "cloud_work_shop"

    storage_client = storage.Client()

    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        imageUri = ("gs://cloud_work_shop/"+blob.name)

        client = vision.ImageAnnotatorClient()
        image = vision.Image()

        image.source.image_uri = imageUri
        objects = client.object_localization(
            image=image).localized_object_annotations

        len(objects)

        for object_ in objects:

            if object_.name == "Cat" and object_.score > 0.80:
                catImg.append('Img Name: {} , Confidence: {}'.format(
                    blob.name, '%.2f%%' % (object_.score*100.)))

            if object_.name == "Dog" and object_.score > 0.80:
                dogImg.append('Img Name: {} , Confidence: {}'.format(
                    blob.name, '%.2f%%' % (object_.score*100.)))

    return render_template('cat-and-dog.html', catImg=catImg, dogImg=dogImg)


@app.route('/callCatDogImgGallery', methods=['GET', 'POST'])
def callCatDogImgGallery():

    catImgUri = []
    dogImgUri = []

    bucket_name = "cloud_work_shop"
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        imageUri = ("gs://cloud_work_shop/"+blob.name)
        publicImgUri = (
            'https://storage.googleapis.com/cloud_work_shop/'+blob.name)

        client = vision.ImageAnnotatorClient()
        image = vision.Image()

        image.source.image_uri = imageUri
        objects = client.object_localization(
            image=image).localized_object_annotations

        len(objects)

        for object_ in objects:

            if object_.name == "Cat" and object_.score > 0.80:
                catImgUri.append(publicImgUri)

            if object_.name == "Dog" and object_.score > 0.80:
                dogImgUri.append(publicImgUri)

    return render_template('cat-and-dog-img-gallery.html', catImgUri=catImgUri, dogImgUri=dogImgUri)


@app.route('/detect-Web-entities', methods=['GET', 'POST'])
def detectWebEntities():

    return render_template('detect-web-entities.html')


@app.route('/upload-image', methods=['GET', 'POST'])
def uploadImage():

    if request.method == 'POST':

        objectName = []
        isEmpty = False
        publicImgUri = ''

        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file == '':
            return redirect(request.url)

        if file:

            print(file)

            storage_client = storage.Client()
            bucket = storage_client.bucket("cloud_work_shop")
            filename = '%s/%s' % ('img', file.filename)

            blob = bucket.blob(filename, chunk_size=262144 * 5)
            blob.upload_from_file(file, file.content_type)

            image_uri = ('gs://cloud_work_shop/img/'+file.filename)
            publicImgUri = (
                "https://storage.googleapis.com/cloud_work_shop/img/"+file.filename)

            client = vision.ImageAnnotatorClient()
            image = vision.Image()
            image.source.image_uri = image_uri

            response = client.web_detection(image=image)
            annotations = response.web_detection

            if annotations.pages_with_matching_images:

                for page in annotations.pages_with_matching_images:
                    objectName.append(format(page.url))

            else:
                isEmpty = True

        return render_template('detect-web-entities.html', objectName=objectName, isEmpty=isEmpty, publicImgUri=publicImgUri)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
