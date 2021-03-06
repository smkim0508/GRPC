# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_sample.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_sample.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12proto_sample.proto\"U\n\x10InferenceRequest\x12\x11\n\timg_bytes\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x0f\n\x07\x63hannel\x18\x04 \x01(\x05\"3\n\x0eInferenceReply\x12\x13\n\x0b\x63lass_index\x18\x01 \x01(\x05\x12\x0c\n\x04prob\x18\x02 \x01(\x02\x32\x42\n\x0f\x41I_ModelService\x12/\n\x07process\x12\x11.InferenceRequest\x1a\x0f.InferenceReply\"\x00\x62\x06proto3'
)




_INFERENCEREQUEST = _descriptor.Descriptor(
  name='InferenceRequest',
  full_name='InferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='img_bytes', full_name='InferenceRequest.img_bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='InferenceRequest.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='InferenceRequest.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='InferenceRequest.channel', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=107,
)


_INFERENCEREPLY = _descriptor.Descriptor(
  name='InferenceReply',
  full_name='InferenceReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_index', full_name='InferenceReply.class_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prob', full_name='InferenceReply.prob', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['InferenceRequest'] = _INFERENCEREQUEST
DESCRIPTOR.message_types_by_name['InferenceReply'] = _INFERENCEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InferenceRequest = _reflection.GeneratedProtocolMessageType('InferenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCEREQUEST,
  '__module__' : 'proto_sample_pb2'
  # @@protoc_insertion_point(class_scope:InferenceRequest)
  })
_sym_db.RegisterMessage(InferenceRequest)

InferenceReply = _reflection.GeneratedProtocolMessageType('InferenceReply', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCEREPLY,
  '__module__' : 'proto_sample_pb2'
  # @@protoc_insertion_point(class_scope:InferenceReply)
  })
_sym_db.RegisterMessage(InferenceReply)



_AI_MODELSERVICE = _descriptor.ServiceDescriptor(
  name='AI_ModelService',
  full_name='AI_ModelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=162,
  serialized_end=228,
  methods=[
  _descriptor.MethodDescriptor(
    name='process',
    full_name='AI_ModelService.process',
    index=0,
    containing_service=None,
    input_type=_INFERENCEREQUEST,
    output_type=_INFERENCEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AI_MODELSERVICE)

DESCRIPTOR.services_by_name['AI_ModelService'] = _AI_MODELSERVICE

# @@protoc_insertion_point(module_scope)
