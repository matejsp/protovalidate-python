# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buf/validate/conformance/cases/enums.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buf.validate.conformance.cases.other_package import embed_pb2 as buf_dot_validate_dot_conformance_dot_cases_dot_other__package_dot_embed__pb2
from buf.validate.conformance.cases.yet_another_package import embed2_pb2 as buf_dot_validate_dot_conformance_dot_cases_dot_yet__another__package_dot_embed2__pb2
from buf.validate import validate_pb2 as buf_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*buf/validate/conformance/cases/enums.proto\x12\x1e\x62uf.validate.conformance.cases\x1a\x38\x62uf/validate/conformance/cases/other_package/embed.proto\x1a?buf/validate/conformance/cases/yet_another_package/embed2.proto\x1a\x1b\x62uf/validate/validate.proto\"F\n\x08\x45numNone\x12:\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumR\x03val\"R\n\tEnumConst\x12\x45\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\t\xfa\xf7\x18\x05\x82\x01\x02\x08\x02R\x03val\"\\\n\x0e\x45numAliasConst\x12J\n\x03val\x18\x01 \x01(\x0e\x32-.buf.validate.conformance.cases.TestEnumAliasB\t\xfa\xf7\x18\x05\x82\x01\x02\x08\x02R\x03val\"T\n\x0b\x45numDefined\x12\x45\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\t\xfa\xf7\x18\x05\x82\x01\x02\x10\x01R\x03val\"^\n\x10\x45numAliasDefined\x12J\n\x03val\x18\x01 \x01(\x0e\x32-.buf.validate.conformance.cases.TestEnumAliasB\t\xfa\xf7\x18\x05\x82\x01\x02\x10\x01R\x03val\"Q\n\x06\x45numIn\x12G\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\x0b\xfa\xf7\x18\x07\x82\x01\x04\x1a\x02\x00\x02R\x03val\"[\n\x0b\x45numAliasIn\x12L\n\x03val\x18\x01 \x01(\x0e\x32-.buf.validate.conformance.cases.TestEnumAliasB\x0b\xfa\xf7\x18\x07\x82\x01\x04\x1a\x02\x00\x02R\x03val\"S\n\tEnumNotIn\x12\x46\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\n\xfa\xf7\x18\x06\x82\x01\x03\"\x01\x01R\x03val\"]\n\x0e\x45numAliasNotIn\x12K\n\x03val\x18\x01 \x01(\x0e\x32-.buf.validate.conformance.cases.TestEnumAliasB\n\xfa\xf7\x18\x06\x82\x01\x03\"\x01\x01R\x03val\"k\n\x0c\x45numExternal\x12[\n\x03val\x18\x01 \x01(\x0e\x32>.buf.validate.conformance.cases.other_package.Embed.EnumeratedB\t\xfa\xf7\x18\x05\x82\x01\x02\x10\x01R\x03val\"~\n\rEnumExternal2\x12m\n\x03val\x18\x01 \x01(\x0e\x32P.buf.validate.conformance.cases.other_package.Embed.DoubleEmbed.DoubleEnumeratedB\t\xfa\xf7\x18\x05\x82\x01\x02\x10\x01R\x03val\"a\n\x13RepeatedEnumDefined\x12J\n\x03val\x18\x01 \x03(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\x0e\xfa\xf7\x18\n\x92\x01\x07\"\x05\x82\x01\x02\x10\x01R\x03val\"\x7f\n\x1bRepeatedExternalEnumDefined\x12`\n\x03val\x18\x01 \x03(\x0e\x32>.buf.validate.conformance.cases.other_package.Embed.EnumeratedB\x0e\xfa\xf7\x18\n\x92\x01\x07\"\x05\x82\x01\x02\x10\x01R\x03val\"\x8f\x01\n%RepeatedYetAnotherExternalEnumDefined\x12\x66\n\x03val\x18\x01 \x03(\x0e\x32\x44.buf.validate.conformance.cases.yet_another_package.Embed.EnumeratedB\x0e\xfa\xf7\x18\n\x92\x01\x07\"\x05\x82\x01\x02\x10\x01R\x03val\"\xcd\x01\n\x0eMapEnumDefined\x12Y\n\x03val\x18\x01 \x03(\x0b\x32\x37.buf.validate.conformance.cases.MapEnumDefined.ValEntryB\x0e\xfa\xf7\x18\n\x9a\x01\x07*\x05\x82\x01\x02\x10\x01R\x03val\x1a`\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12>\n\x05value\x18\x02 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumR\x05value:\x02\x38\x01\"\xf3\x01\n\x16MapExternalEnumDefined\x12\x61\n\x03val\x18\x01 \x03(\x0b\x32?.buf.validate.conformance.cases.MapExternalEnumDefined.ValEntryB\x0e\xfa\xf7\x18\n\x9a\x01\x07*\x05\x82\x01\x02\x10\x01R\x03val\x1av\n\x08ValEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12T\n\x05value\x18\x02 \x01(\x0e\x32>.buf.validate.conformance.cases.other_package.Embed.EnumeratedR\x05value:\x02\x38\x01\"\xb6\x01\n\x0f\x45numInsideOneof\x12G\n\x03val\x18\x01 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\t\xfa\xf7\x18\x05\x82\x01\x02\x10\x01H\x00R\x03val\x12L\n\x04val2\x18\x02 \x01(\x0e\x32(.buf.validate.conformance.cases.TestEnumB\x0c\xfa\xf7\x18\x08\x82\x01\x05\x10\x01\"\x01\x00H\x01R\x04val2B\x05\n\x03\x66ooB\x05\n\x03\x62\x61r*K\n\x08TestEnum\x12\x19\n\x15TEST_ENUM_UNSPECIFIED\x10\x00\x12\x11\n\rTEST_ENUM_ONE\x10\x01\x12\x11\n\rTEST_ENUM_TWO\x10\x02*\xc9\x01\n\rTestEnumAlias\x12\x1f\n\x1bTEST_ENUM_ALIAS_UNSPECIFIED\x10\x00\x12\x15\n\x11TEST_ENUM_ALIAS_A\x10\x01\x12\x15\n\x11TEST_ENUM_ALIAS_B\x10\x02\x12\x15\n\x11TEST_ENUM_ALIAS_C\x10\x03\x12\x19\n\x15TEST_ENUM_ALIAS_ALPHA\x10\x01\x12\x18\n\x14TEST_ENUM_ALIAS_BETA\x10\x02\x12\x19\n\x15TEST_ENUM_ALIAS_GAMMA\x10\x03\x1a\x02\x10\x01\x42\xa1\x02\n\"com.buf.validate.conformance.casesB\nEnumsProtoP\x01ZSgithub.com/bufbuild/protovalidate/tools/internal/gen/buf/validate/conformance/cases\xa2\x02\x04\x42VCC\xaa\x02\x1e\x42uf.Validate.Conformance.Cases\xca\x02\x1e\x42uf\\Validate\\Conformance\\Cases\xe2\x02*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\xea\x02!Buf::Validate::Conformance::Casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'buf.validate.conformance.cases.enums_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"com.buf.validate.conformance.casesB\nEnumsProtoP\001ZSgithub.com/bufbuild/protovalidate/tools/internal/gen/buf/validate/conformance/cases\242\002\004BVCC\252\002\036Buf.Validate.Conformance.Cases\312\002\036Buf\\Validate\\Conformance\\Cases\342\002*Buf\\Validate\\Conformance\\Cases\\GPBMetadata\352\002!Buf::Validate::Conformance::Cases'
  _TESTENUMALIAS._options = None
  _TESTENUMALIAS._serialized_options = b'\020\001'
  _ENUMCONST.fields_by_name['val']._options = None
  _ENUMCONST.fields_by_name['val']._serialized_options = b'\372\367\030\005\202\001\002\010\002'
  _ENUMALIASCONST.fields_by_name['val']._options = None
  _ENUMALIASCONST.fields_by_name['val']._serialized_options = b'\372\367\030\005\202\001\002\010\002'
  _ENUMDEFINED.fields_by_name['val']._options = None
  _ENUMDEFINED.fields_by_name['val']._serialized_options = b'\372\367\030\005\202\001\002\020\001'
  _ENUMALIASDEFINED.fields_by_name['val']._options = None
  _ENUMALIASDEFINED.fields_by_name['val']._serialized_options = b'\372\367\030\005\202\001\002\020\001'
  _ENUMIN.fields_by_name['val']._options = None
  _ENUMIN.fields_by_name['val']._serialized_options = b'\372\367\030\007\202\001\004\032\002\000\002'
  _ENUMALIASIN.fields_by_name['val']._options = None
  _ENUMALIASIN.fields_by_name['val']._serialized_options = b'\372\367\030\007\202\001\004\032\002\000\002'
  _ENUMNOTIN.fields_by_name['val']._options = None
  _ENUMNOTIN.fields_by_name['val']._serialized_options = b'\372\367\030\006\202\001\003\"\001\001'
  _ENUMALIASNOTIN.fields_by_name['val']._options = None
  _ENUMALIASNOTIN.fields_by_name['val']._serialized_options = b'\372\367\030\006\202\001\003\"\001\001'
  _ENUMEXTERNAL.fields_by_name['val']._options = None
  _ENUMEXTERNAL.fields_by_name['val']._serialized_options = b'\372\367\030\005\202\001\002\020\001'
  _ENUMEXTERNAL2.fields_by_name['val']._options = None
  _ENUMEXTERNAL2.fields_by_name['val']._serialized_options = b'\372\367\030\005\202\001\002\020\001'
  _REPEATEDENUMDEFINED.fields_by_name['val']._options = None
  _REPEATEDENUMDEFINED.fields_by_name['val']._serialized_options = b'\372\367\030\n\222\001\007\"\005\202\001\002\020\001'
  _REPEATEDEXTERNALENUMDEFINED.fields_by_name['val']._options = None
  _REPEATEDEXTERNALENUMDEFINED.fields_by_name['val']._serialized_options = b'\372\367\030\n\222\001\007\"\005\202\001\002\020\001'
  _REPEATEDYETANOTHEREXTERNALENUMDEFINED.fields_by_name['val']._options = None
  _REPEATEDYETANOTHEREXTERNALENUMDEFINED.fields_by_name['val']._serialized_options = b'\372\367\030\n\222\001\007\"\005\202\001\002\020\001'
  _MAPENUMDEFINED_VALENTRY._options = None
  _MAPENUMDEFINED_VALENTRY._serialized_options = b'8\001'
  _MAPENUMDEFINED.fields_by_name['val']._options = None
  _MAPENUMDEFINED.fields_by_name['val']._serialized_options = b'\372\367\030\n\232\001\007*\005\202\001\002\020\001'
  _MAPEXTERNALENUMDEFINED_VALENTRY._options = None
  _MAPEXTERNALENUMDEFINED_VALENTRY._serialized_options = b'8\001'
  _MAPEXTERNALENUMDEFINED.fields_by_name['val']._options = None
  _MAPEXTERNALENUMDEFINED.fields_by_name['val']._serialized_options = b'\372\367\030\n\232\001\007*\005\202\001\002\020\001'
  _ENUMINSIDEONEOF.fields_by_name['val']._options = None
  _ENUMINSIDEONEOF.fields_by_name['val']._serialized_options = b'\372\367\030\005\202\001\002\020\001'
  _ENUMINSIDEONEOF.fields_by_name['val2']._options = None
  _ENUMINSIDEONEOF.fields_by_name['val2']._serialized_options = b'\372\367\030\010\202\001\005\020\001\"\001\000'
  _globals['_TESTENUM']._serialized_start=2268
  _globals['_TESTENUM']._serialized_end=2343
  _globals['_TESTENUMALIAS']._serialized_start=2346
  _globals['_TESTENUMALIAS']._serialized_end=2547
  _globals['_ENUMNONE']._serialized_start=230
  _globals['_ENUMNONE']._serialized_end=300
  _globals['_ENUMCONST']._serialized_start=302
  _globals['_ENUMCONST']._serialized_end=384
  _globals['_ENUMALIASCONST']._serialized_start=386
  _globals['_ENUMALIASCONST']._serialized_end=478
  _globals['_ENUMDEFINED']._serialized_start=480
  _globals['_ENUMDEFINED']._serialized_end=564
  _globals['_ENUMALIASDEFINED']._serialized_start=566
  _globals['_ENUMALIASDEFINED']._serialized_end=660
  _globals['_ENUMIN']._serialized_start=662
  _globals['_ENUMIN']._serialized_end=743
  _globals['_ENUMALIASIN']._serialized_start=745
  _globals['_ENUMALIASIN']._serialized_end=836
  _globals['_ENUMNOTIN']._serialized_start=838
  _globals['_ENUMNOTIN']._serialized_end=921
  _globals['_ENUMALIASNOTIN']._serialized_start=923
  _globals['_ENUMALIASNOTIN']._serialized_end=1016
  _globals['_ENUMEXTERNAL']._serialized_start=1018
  _globals['_ENUMEXTERNAL']._serialized_end=1125
  _globals['_ENUMEXTERNAL2']._serialized_start=1127
  _globals['_ENUMEXTERNAL2']._serialized_end=1253
  _globals['_REPEATEDENUMDEFINED']._serialized_start=1255
  _globals['_REPEATEDENUMDEFINED']._serialized_end=1352
  _globals['_REPEATEDEXTERNALENUMDEFINED']._serialized_start=1354
  _globals['_REPEATEDEXTERNALENUMDEFINED']._serialized_end=1481
  _globals['_REPEATEDYETANOTHEREXTERNALENUMDEFINED']._serialized_start=1484
  _globals['_REPEATEDYETANOTHEREXTERNALENUMDEFINED']._serialized_end=1627
  _globals['_MAPENUMDEFINED']._serialized_start=1630
  _globals['_MAPENUMDEFINED']._serialized_end=1835
  _globals['_MAPENUMDEFINED_VALENTRY']._serialized_start=1739
  _globals['_MAPENUMDEFINED_VALENTRY']._serialized_end=1835
  _globals['_MAPEXTERNALENUMDEFINED']._serialized_start=1838
  _globals['_MAPEXTERNALENUMDEFINED']._serialized_end=2081
  _globals['_MAPEXTERNALENUMDEFINED_VALENTRY']._serialized_start=1963
  _globals['_MAPEXTERNALENUMDEFINED_VALENTRY']._serialized_end=2081
  _globals['_ENUMINSIDEONEOF']._serialized_start=2084
  _globals['_ENUMINSIDEONEOF']._serialized_end=2266
# @@protoc_insertion_point(module_scope)
