# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/priv/private.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x62uf/validate/priv/private.proto\x12\x11\x62uf.validate.priv\x1a google/protobuf/descriptor.proto\"C\n\x10\x46ieldConstraints\x12/\n\x03\x63\x65l\x18\x01 \x03(\x0b\x32\x1d.buf.validate.priv.ConstraintR\x03\x63\x65l\"V\n\nConstraint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x1e\n\nexpression\x18\x03 \x01(\tR\nexpression:]\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\x80\x8f\x03 \x01(\x0b\x32#.buf.validate.priv.FieldConstraintsR\x05\x66ield\x88\x01\x01\x42NZLbuf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate/privb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.priv.private_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZLbuf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate/priv'
  _globals['_FIELDCONSTRAINTS']._serialized_start=88
  _globals['_FIELDCONSTRAINTS']._serialized_end=155
  _globals['_CONSTRAINT']._serialized_start=157
  _globals['_CONSTRAINT']._serialized_end=243
# @@protoc_insertion_point(module_scope)
