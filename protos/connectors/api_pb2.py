# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos.connectors import connector_pb2 as protos_dot_connectors_dot_connector__pb2
from protos import base_pb2 as protos_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bprotos/connectors/api.proto\x12\x11protos.connectors\x1a\x1egoogle/protobuf/wrappers.proto\x1a!protos/connectors/connector.proto\x1a\x11protos/base.proto\"\x82\x01\n\x16\x43reateConnectorRequest\x12/\n\tconnector\x18\x01 \x01(\x0b\x32\x1c.protos.connectors.Connector\x12\x37\n\x0e\x63onnector_keys\x18\x02 \x03(\x0b\x32\x1f.protos.connectors.ConnectorKey\"h\n\x17\x43reateConnectorResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"\x1a\n\x18GetConnectorsListRequest\"\x92\x02\n\x19GetConnectorsListResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12\x38\n\x12request_connectors\x18\x03 \x03(\x0b\x32\x1c.protos.connectors.Connector\x12:\n\x14\x61vailable_connectors\x18\x04 \x03(\x0b\x32\x1c.protos.connectors.Connector\x12\x30\n\nconnectors\x18\x05 \x03(\x0b\x32\x1c.protos.connectors.Connector\"\x90\x01\n\x16UpdateConnectorRequest\x12\x32\n\x0c\x63onnector_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x42\n\x14update_connector_ops\x18\x02 \x03(\x0b\x32$.protos.connectors.UpdateConnectorOp\"h\n\x17UpdateConnectorResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\"Z\n\x1eGetConnectorKeysOptionsRequest\x12\x38\n\x0e\x63onnector_type\x18\x01 \x01(\x0e\x32 .protos.connectors.ConnectorType\"\xb0\x01\n\x1fGetConnectorKeysOptionsResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12>\n\x15\x63onnector_key_options\x18\x03 \x03(\x0b\x32\x1f.protos.connectors.ConnectorKey\"\x87\x01\n\x17GetConnectorKeysRequest\x12\x32\n\x0c\x63onnector_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x38\n\x0e\x63onnector_type\x18\x02 \x01(\x0e\x32 .protos.connectors.ConnectorType\"\xd3\x01\n\x18GetConnectorKeysResponse\x12+\n\x07success\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12 \n\x07message\x18\x02 \x01(\x0b\x32\x0f.protos.Message\x12/\n\tconnector\x18\x03 \x01(\x0b\x32\x1c.protos.connectors.Connector\x12\x37\n\x0e\x63onnector_keys\x18\x04 \x03(\x0b\x32\x1f.protos.connectors.ConnectorKeyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATECONNECTORREQUEST._serialized_start=137
  _CREATECONNECTORREQUEST._serialized_end=267
  _CREATECONNECTORRESPONSE._serialized_start=269
  _CREATECONNECTORRESPONSE._serialized_end=373
  _GETCONNECTORSLISTREQUEST._serialized_start=375
  _GETCONNECTORSLISTREQUEST._serialized_end=401
  _GETCONNECTORSLISTRESPONSE._serialized_start=404
  _GETCONNECTORSLISTRESPONSE._serialized_end=678
  _UPDATECONNECTORREQUEST._serialized_start=681
  _UPDATECONNECTORREQUEST._serialized_end=825
  _UPDATECONNECTORRESPONSE._serialized_start=827
  _UPDATECONNECTORRESPONSE._serialized_end=931
  _GETCONNECTORKEYSOPTIONSREQUEST._serialized_start=933
  _GETCONNECTORKEYSOPTIONSREQUEST._serialized_end=1023
  _GETCONNECTORKEYSOPTIONSRESPONSE._serialized_start=1026
  _GETCONNECTORKEYSOPTIONSRESPONSE._serialized_end=1202
  _GETCONNECTORKEYSREQUEST._serialized_start=1205
  _GETCONNECTORKEYSREQUEST._serialized_end=1340
  _GETCONNECTORKEYSRESPONSE._serialized_start=1343
  _GETCONNECTORKEYSRESPONSE._serialized_end=1554
# @@protoc_insertion_point(module_scope)
