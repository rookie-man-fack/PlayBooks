"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import protos.base_pb2
import protos.connectors.connector_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SshServerAssetModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        name: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["name", b"name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___SshServerAssetModel = SshServerAssetModel

@typing_extensions.final
class SshServerAssetOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SSH_SERVERS_FIELD_NUMBER: builtins.int
    @property
    def ssh_servers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        ssh_servers: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ssh_servers", b"ssh_servers"]) -> None: ...

global___SshServerAssetOptions = SshServerAssetOptions

@typing_extensions.final
class RemoteServerAssetModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LAST_UPDATED_FIELD_NUMBER: builtins.int
    SSH_SERVER_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    connector_type: protos.base_pb2.Source.ValueType
    type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType
    last_updated: builtins.int
    @property
    def ssh_server(self) -> global___SshServerAssetModel: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        connector_type: protos.base_pb2.Source.ValueType = ...,
        type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType = ...,
        last_updated: builtins.int = ...,
        ssh_server: global___SshServerAssetModel | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["asset", b"asset", "id", b"id", "ssh_server", b"ssh_server"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset", b"asset", "connector_type", b"connector_type", "id", b"id", "last_updated", b"last_updated", "ssh_server", b"ssh_server", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["asset", b"asset"]) -> typing_extensions.Literal["ssh_server"] | None: ...

global___RemoteServerAssetModel = RemoteServerAssetModel

@typing_extensions.final
class RemoteServerAssets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSETS_FIELD_NUMBER: builtins.int
    @property
    def assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RemoteServerAssetModel]: ...
    def __init__(
        self,
        *,
        assets: collections.abc.Iterable[global___RemoteServerAssetModel] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assets", b"assets"]) -> None: ...

global___RemoteServerAssets = RemoteServerAssets