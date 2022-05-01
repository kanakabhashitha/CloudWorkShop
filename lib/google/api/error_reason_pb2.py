# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/error_reason.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/api/error_reason.proto",
    package="google.api",
    syntax="proto3",
    serialized_options=b"\n\016com.google.apiB\020ErrorReasonProtoP\001ZCgoogle.golang.org/genproto/googleapis/api/error_reason;error_reason\242\002\004GAPI",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n\x1dgoogle/api/error_reason.proto\x12\ngoogle.api*\xc4\x04\n\x0b\x45rrorReason\x12\x1c\n\x18\x45RROR_REASON_UNSPECIFIED\x10\x00\x12\x14\n\x10SERVICE_DISABLED\x10\x01\x12\x14\n\x10\x42ILLING_DISABLED\x10\x02\x12\x13\n\x0f\x41PI_KEY_INVALID\x10\x03\x12\x1b\n\x17\x41PI_KEY_SERVICE_BLOCKED\x10\x04\x12!\n\x1d\x41PI_KEY_HTTP_REFERRER_BLOCKED\x10\x07\x12\x1e\n\x1a\x41PI_KEY_IP_ADDRESS_BLOCKED\x10\x08\x12\x1f\n\x1b\x41PI_KEY_ANDROID_APP_BLOCKED\x10\t\x12\x1b\n\x17\x41PI_KEY_IOS_APP_BLOCKED\x10\r\x12\x17\n\x13RATE_LIMIT_EXCEEDED\x10\x05\x12\x1b\n\x17RESOURCE_QUOTA_EXCEEDED\x10\x06\x12 \n\x1cLOCATION_TAX_POLICY_VIOLATED\x10\n\x12\x17\n\x13USER_PROJECT_DENIED\x10\x0b\x12\x16\n\x12\x43ONSUMER_SUSPENDED\x10\x0c\x12\x14\n\x10\x43ONSUMER_INVALID\x10\x0e\x12\x1c\n\x18SECURITY_POLICY_VIOLATED\x10\x0f\x12\x18\n\x14\x41\x43\x43\x45SS_TOKEN_EXPIRED\x10\x10\x12#\n\x1f\x41\x43\x43\x45SS_TOKEN_SCOPE_INSUFFICIENT\x10\x11\x12\x19\n\x15\x41\x43\x43OUNT_STATE_INVALID\x10\x12\x12!\n\x1d\x41\x43\x43\x45SS_TOKEN_TYPE_UNSUPPORTED\x10\x13\x42p\n\x0e\x63om.google.apiB\x10\x45rrorReasonProtoP\x01ZCgoogle.golang.org/genproto/googleapis/api/error_reason;error_reason\xa2\x02\x04GAPIb\x06proto3",
)

_ERRORREASON = _descriptor.EnumDescriptor(
    name="ErrorReason",
    full_name="google.api.ErrorReason",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ERROR_REASON_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SERVICE_DISABLED",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BILLING_DISABLED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="API_KEY_INVALID",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="API_KEY_SERVICE_BLOCKED",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="API_KEY_HTTP_REFERRER_BLOCKED",
            index=5,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="API_KEY_IP_ADDRESS_BLOCKED",
            index=6,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="API_KEY_ANDROID_APP_BLOCKED",
            index=7,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="API_KEY_IOS_APP_BLOCKED",
            index=8,
            number=13,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RATE_LIMIT_EXCEEDED",
            index=9,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RESOURCE_QUOTA_EXCEEDED",
            index=10,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="LOCATION_TAX_POLICY_VIOLATED",
            index=11,
            number=10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="USER_PROJECT_DENIED",
            index=12,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONSUMER_SUSPENDED",
            index=13,
            number=12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONSUMER_INVALID",
            index=14,
            number=14,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SECURITY_POLICY_VIOLATED",
            index=15,
            number=15,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACCESS_TOKEN_EXPIRED",
            index=16,
            number=16,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACCESS_TOKEN_SCOPE_INSUFFICIENT",
            index=17,
            number=17,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACCOUNT_STATE_INVALID",
            index=18,
            number=18,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACCESS_TOKEN_TYPE_UNSUPPORTED",
            index=19,
            number=19,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=46,
    serialized_end=626,
)
_sym_db.RegisterEnumDescriptor(_ERRORREASON)

ErrorReason = enum_type_wrapper.EnumTypeWrapper(_ERRORREASON)
ERROR_REASON_UNSPECIFIED = 0
SERVICE_DISABLED = 1
BILLING_DISABLED = 2
API_KEY_INVALID = 3
API_KEY_SERVICE_BLOCKED = 4
API_KEY_HTTP_REFERRER_BLOCKED = 7
API_KEY_IP_ADDRESS_BLOCKED = 8
API_KEY_ANDROID_APP_BLOCKED = 9
API_KEY_IOS_APP_BLOCKED = 13
RATE_LIMIT_EXCEEDED = 5
RESOURCE_QUOTA_EXCEEDED = 6
LOCATION_TAX_POLICY_VIOLATED = 10
USER_PROJECT_DENIED = 11
CONSUMER_SUSPENDED = 12
CONSUMER_INVALID = 14
SECURITY_POLICY_VIOLATED = 15
ACCESS_TOKEN_EXPIRED = 16
ACCESS_TOKEN_SCOPE_INSUFFICIENT = 17
ACCOUNT_STATE_INVALID = 18
ACCESS_TOKEN_TYPE_UNSUPPORTED = 19


DESCRIPTOR.enum_types_by_name["ErrorReason"] = _ERRORREASON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)