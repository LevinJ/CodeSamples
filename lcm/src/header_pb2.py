# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: header.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='header.proto',
  package='atd.common',
  syntax='proto2',
  serialized_pb=_b('\n\x0cheader.proto\x12\natd.common\"J\n\x06header\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x12\x13\n\x0bmodule_name\x18\x02 \x01(\t\x12\x14\n\x0csequence_num\x18\x03 \x01(\r\"0\n\ttimestamp\x12\x15\n\rtimestamp_sec\x18\x01 \x01(\x01\x12\x0c\n\x04type\x18\x02 \x01(\x05\x42\x02H\x03')
)




_HEADER = _descriptor.Descriptor(
  name='header',
  full_name='atd.common.header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_sec', full_name='atd.common.header.timestamp_sec', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='module_name', full_name='atd.common.header.module_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence_num', full_name='atd.common.header.sequence_num', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=102,
)


_TIMESTAMP = _descriptor.Descriptor(
  name='timestamp',
  full_name='atd.common.timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_sec', full_name='atd.common.timestamp.timestamp_sec', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='atd.common.timestamp.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=152,
)

DESCRIPTOR.message_types_by_name['header'] = _HEADER
DESCRIPTOR.message_types_by_name['timestamp'] = _TIMESTAMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

header = _reflection.GeneratedProtocolMessageType('header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'header_pb2'
  # @@protoc_insertion_point(class_scope:atd.common.header)
  ))
_sym_db.RegisterMessage(header)

timestamp = _reflection.GeneratedProtocolMessageType('timestamp', (_message.Message,), dict(
  DESCRIPTOR = _TIMESTAMP,
  __module__ = 'header_pb2'
  # @@protoc_insertion_point(class_scope:atd.common.timestamp)
  ))
_sym_db.RegisterMessage(timestamp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
