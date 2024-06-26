"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class SlackChannelAlertEntryPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLACK_CHANNEL_ID_FIELD_NUMBER: builtins.int
    SLACK_CHANNEL_NAME_FIELD_NUMBER: builtins.int
    SLACK_ALERT_TYPE_FIELD_NUMBER: builtins.int
    SLACK_ALERT_FILTER_STRING_FIELD_NUMBER: builtins.int
    @property
    def slack_channel_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def slack_channel_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def slack_alert_type(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def slack_alert_filter_string(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        slack_channel_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        slack_channel_name: google.protobuf.wrappers_pb2.StringValue | None = ...,
        slack_alert_type: google.protobuf.wrappers_pb2.StringValue | None = ...,
        slack_alert_filter_string: google.protobuf.wrappers_pb2.StringValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["slack_alert_filter_string", b"slack_alert_filter_string", "slack_alert_type", b"slack_alert_type", "slack_channel_id", b"slack_channel_id", "slack_channel_name", b"slack_channel_name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["slack_alert_filter_string", b"slack_alert_filter_string", "slack_alert_type", b"slack_alert_type", "slack_channel_id", b"slack_channel_id", "slack_channel_name", b"slack_channel_name"]) -> None: ...

global___SlackChannelAlertEntryPoint = SlackChannelAlertEntryPoint
