# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/connectors/assets/remote_server_asset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from protos import base_pb2 as protos_dot_base__pb2
from protos.connectors import connector_pb2 as protos_dot_connectors_dot_connector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2protos/connectors/assets/remote_server_asset.proto\x12\x18protos.connectors.assets\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x11protos/base.proto\x1a!protos/connectors/connector.proto\"A\n\x13SshServerAssetModel\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\",\n\x15SshServerAssetOptions\x12\x13\n\x0bssh_servers\x18\x01 \x03(\t\"\xf5\x01\n\x16RemoteServerAssetModel\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12&\n\x0e\x63onnector_type\x18\x02 \x01(\x0e\x32\x0e.protos.Source\x12%\n\x04type\x18\x03 \x01(\x0e\x32\x17.protos.SourceModelType\x12\x14\n\x0clast_updated\x18\x04 \x01(\x10\x12\x43\n\nssh_server\x18\x05 \x01(\x0b\x32-.protos.connectors.assets.SshServerAssetModelH\x00\x42\x07\n\x05\x61sset\"V\n\x12RemoteServerAssets\x12@\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\x30.protos.connectors.assets.RemoteServerAssetModelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.connectors.assets.remote_server_asset_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SSHSERVERASSETMODEL._serialized_start=166
  _SSHSERVERASSETMODEL._serialized_end=231
  _SSHSERVERASSETOPTIONS._serialized_start=233
  _SSHSERVERASSETOPTIONS._serialized_end=277
  _REMOTESERVERASSETMODEL._serialized_start=280
  _REMOTESERVERASSETMODEL._serialized_end=525
  _REMOTESERVERASSETS._serialized_start=527
  _REMOTESERVERASSETS._serialized_end=613
# @@protoc_insertion_point(module_scope)
