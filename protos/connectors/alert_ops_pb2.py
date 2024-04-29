# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/alert_ops.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!protos/connectors/alert_ops.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xd4\x01\n\rCommWorkspace\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12%\n\x0f\x61\x63tive_channels\x18\x03 \x03(\x0b\x32\x0c.CommChannel\x12#\n\x0b\x61lert_types\x18\x04 \x03(\x0b\x32\x0e.CommAlertType\x12!\n\nalert_tags\x18\x05 \x03(\x0b\x32\r.CommAlertTag\"\x9d\x01\n\x0b\x43ommChannel\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x30\n\nchannel_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x63hannel_name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x9d\x01\n\rCommAlertType\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x30\n\nchannel_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nalert_type\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xd7\x01\n\x0c\x43ommAlertTag\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x37\n\x11\x61\x63tive_channel_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x33\n\ralert_type_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12/\n\talert_tag\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"9\n\x13\x43ommAlertOpsOptions\x12\"\n\nworkspaces\x18\x01 \x03(\x0b\x32\x0e.CommWorkspace\"=\n\x0f\x41lertOpsOptions\x12*\n\x0c\x63omm_options\x18\x01 \x01(\x0b\x32\x14.CommAlertOpsOptions\"\x99\x03\n\nSlackAlert\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x30\n\nalert_type\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x61lert_title\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nalert_text\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12#\n\rslack_channel\x18\x05 \x01(\x0b\x32\x0c.CommChannel\x12\x17\n\x0f\x61lert_timestamp\x18\x06 \x01(\x10\x12(\n\nalert_tags\x18\x07 \x03(\x0b\x32\x14.SlackAlert.AlertTag\x1a\x62\n\x08\x41lertTag\x12)\n\x03key\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.alert_ops_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMMWORKSPACE._serialized_start=103
  _COMMWORKSPACE._serialized_end=315
  _COMMCHANNEL._serialized_start=318
  _COMMCHANNEL._serialized_end=475
  _COMMALERTTYPE._serialized_start=478
  _COMMALERTTYPE._serialized_end=635
  _COMMALERTTAG._serialized_start=638
  _COMMALERTTAG._serialized_end=853
  _COMMALERTOPSOPTIONS._serialized_start=855
  _COMMALERTOPSOPTIONS._serialized_end=912
  _ALERTOPSOPTIONS._serialized_start=914
  _ALERTOPSOPTIONS._serialized_end=975
  _SLACKALERT._serialized_start=978
  _SLACKALERT._serialized_end=1387
  _SLACKALERT_ALERTTAG._serialized_start=1289
  _SLACKALERT_ALERTTAG._serialized_end=1387
# @@protoc_insertion_point(module_scope)