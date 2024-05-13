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
class GrafanaTargetMetricPromQlAssetModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class PromqlMetric(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class QueryVariableValueOptions(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            VARIABLE_FIELD_NUMBER: builtins.int
            VALUES_FIELD_NUMBER: builtins.int
            @property
            def variable(self) -> google.protobuf.wrappers_pb2.StringValue: ...
            @property
            def values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
            def __init__(
                self,
                *,
                variable: google.protobuf.wrappers_pb2.StringValue | None = ...,
                values: collections.abc.Iterable[builtins.str] | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["variable", b"variable"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["values", b"values", "variable", b"variable"]) -> None: ...

        @typing_extensions.final
        class QueryLabelVariableMap(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            LABEL_FIELD_NUMBER: builtins.int
            VARIABLE_FIELD_NUMBER: builtins.int
            @property
            def label(self) -> google.protobuf.wrappers_pb2.StringValue: ...
            @property
            def variable(self) -> google.protobuf.wrappers_pb2.StringValue: ...
            def __init__(
                self,
                *,
                label: google.protobuf.wrappers_pb2.StringValue | None = ...,
                variable: google.protobuf.wrappers_pb2.StringValue | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["label", b"label", "variable", b"variable"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["label", b"label", "variable", b"variable"]) -> None: ...

        TARGET_METRIC_REF_ID_FIELD_NUMBER: builtins.int
        DATASOURCE_UID_FIELD_NUMBER: builtins.int
        EXPRESSION_FIELD_NUMBER: builtins.int
        LABEL_VARIABLE_MAP_FIELD_NUMBER: builtins.int
        VARIABLE_VALUES_OPTIONS_FIELD_NUMBER: builtins.int
        @property
        def target_metric_ref_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def datasource_uid(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def expression(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def label_variable_map(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GrafanaTargetMetricPromQlAssetModel.PromqlMetric.QueryLabelVariableMap]: ...
        @property
        def variable_values_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GrafanaTargetMetricPromQlAssetModel.PromqlMetric.QueryVariableValueOptions]: ...
        def __init__(
            self,
            *,
            target_metric_ref_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
            datasource_uid: google.protobuf.wrappers_pb2.StringValue | None = ...,
            expression: google.protobuf.wrappers_pb2.StringValue | None = ...,
            label_variable_map: collections.abc.Iterable[global___GrafanaTargetMetricPromQlAssetModel.PromqlMetric.QueryLabelVariableMap] | None = ...,
            variable_values_options: collections.abc.Iterable[global___GrafanaTargetMetricPromQlAssetModel.PromqlMetric.QueryVariableValueOptions] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["datasource_uid", b"datasource_uid", "expression", b"expression", "target_metric_ref_id", b"target_metric_ref_id"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["datasource_uid", b"datasource_uid", "expression", b"expression", "label_variable_map", b"label_variable_map", "target_metric_ref_id", b"target_metric_ref_id", "variable_values_options", b"variable_values_options"]) -> None: ...

    @typing_extensions.final
    class PanelPromqlMap(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PANEL_ID_FIELD_NUMBER: builtins.int
        PANEL_TITLE_FIELD_NUMBER: builtins.int
        PROMQL_METRICS_FIELD_NUMBER: builtins.int
        @property
        def panel_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def panel_title(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def promql_metrics(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GrafanaTargetMetricPromQlAssetModel.PromqlMetric]: ...
        def __init__(
            self,
            *,
            panel_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
            panel_title: google.protobuf.wrappers_pb2.StringValue | None = ...,
            promql_metrics: collections.abc.Iterable[global___GrafanaTargetMetricPromQlAssetModel.PromqlMetric] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["panel_id", b"panel_id", "panel_title", b"panel_title"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["panel_id", b"panel_id", "panel_title", b"panel_title", "promql_metrics", b"promql_metrics"]) -> None: ...

    DASHBOARD_ID_FIELD_NUMBER: builtins.int
    DASHBOARD_TITLE_FIELD_NUMBER: builtins.int
    DASHBOARD_URL_FIELD_NUMBER: builtins.int
    PANEL_PROMQL_MAP_FIELD_NUMBER: builtins.int
    @property
    def dashboard_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def dashboard_title(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def dashboard_url(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def panel_promql_map(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GrafanaTargetMetricPromQlAssetModel.PanelPromqlMap]: ...
    def __init__(
        self,
        *,
        dashboard_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
        dashboard_title: google.protobuf.wrappers_pb2.StringValue | None = ...,
        dashboard_url: google.protobuf.wrappers_pb2.StringValue | None = ...,
        panel_promql_map: collections.abc.Iterable[global___GrafanaTargetMetricPromQlAssetModel.PanelPromqlMap] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dashboard_id", b"dashboard_id", "dashboard_title", b"dashboard_title", "dashboard_url", b"dashboard_url"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["dashboard_id", b"dashboard_id", "dashboard_title", b"dashboard_title", "dashboard_url", b"dashboard_url", "panel_promql_map", b"panel_promql_map"]) -> None: ...

global___GrafanaTargetMetricPromQlAssetModel = GrafanaTargetMetricPromQlAssetModel

@typing_extensions.final
class GrafanaTargetMetricPromQlAssetOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class GrafanaDashboardOptions(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class GrafanaPanelOptions(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            PANEL_ID_FIELD_NUMBER: builtins.int
            PANEL_TITLE_FIELD_NUMBER: builtins.int
            @property
            def panel_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
            @property
            def panel_title(self) -> google.protobuf.wrappers_pb2.StringValue: ...
            def __init__(
                self,
                *,
                panel_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
                panel_title: google.protobuf.wrappers_pb2.StringValue | None = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["panel_id", b"panel_id", "panel_title", b"panel_title"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["panel_id", b"panel_id", "panel_title", b"panel_title"]) -> None: ...

        DASHBOARD_ID_FIELD_NUMBER: builtins.int
        DASHBOARD_TITLE_FIELD_NUMBER: builtins.int
        DASHBOARD_URL_FIELD_NUMBER: builtins.int
        PANEL_OPTIONS_FIELD_NUMBER: builtins.int
        @property
        def dashboard_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def dashboard_title(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def dashboard_url(self) -> google.protobuf.wrappers_pb2.StringValue: ...
        @property
        def panel_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GrafanaTargetMetricPromQlAssetOptions.GrafanaDashboardOptions.GrafanaPanelOptions]: ...
        def __init__(
            self,
            *,
            dashboard_id: google.protobuf.wrappers_pb2.StringValue | None = ...,
            dashboard_title: google.protobuf.wrappers_pb2.StringValue | None = ...,
            dashboard_url: google.protobuf.wrappers_pb2.StringValue | None = ...,
            panel_options: collections.abc.Iterable[global___GrafanaTargetMetricPromQlAssetOptions.GrafanaDashboardOptions.GrafanaPanelOptions] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["dashboard_id", b"dashboard_id", "dashboard_title", b"dashboard_title", "dashboard_url", b"dashboard_url"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["dashboard_id", b"dashboard_id", "dashboard_title", b"dashboard_title", "dashboard_url", b"dashboard_url", "panel_options", b"panel_options"]) -> None: ...

    DASHBOARDS_FIELD_NUMBER: builtins.int
    @property
    def dashboards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GrafanaTargetMetricPromQlAssetOptions.GrafanaDashboardOptions]: ...
    def __init__(
        self,
        *,
        dashboards: collections.abc.Iterable[global___GrafanaTargetMetricPromQlAssetOptions.GrafanaDashboardOptions] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dashboards", b"dashboards"]) -> None: ...

global___GrafanaTargetMetricPromQlAssetOptions = GrafanaTargetMetricPromQlAssetOptions

@typing_extensions.final
class GrafanaAssetModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CONNECTOR_TYPE_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LAST_UPDATED_FIELD_NUMBER: builtins.int
    GRAFANA_TARGET_METRIC_PROMQL_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> google.protobuf.wrappers_pb2.UInt64Value: ...
    connector_type: protos.base_pb2.Source.ValueType
    type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType
    last_updated: builtins.int
    @property
    def grafana_target_metric_promql(self) -> global___GrafanaTargetMetricPromQlAssetModel: ...
    def __init__(
        self,
        *,
        id: google.protobuf.wrappers_pb2.UInt64Value | None = ...,
        connector_type: protos.base_pb2.Source.ValueType = ...,
        type: protos.connectors.connector_pb2.ConnectorMetadataModelType.ValueType = ...,
        last_updated: builtins.int = ...,
        grafana_target_metric_promql: global___GrafanaTargetMetricPromQlAssetModel | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["asset", b"asset", "grafana_target_metric_promql", b"grafana_target_metric_promql", "id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset", b"asset", "connector_type", b"connector_type", "grafana_target_metric_promql", b"grafana_target_metric_promql", "id", b"id", "last_updated", b"last_updated", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["asset", b"asset"]) -> typing_extensions.Literal["grafana_target_metric_promql"] | None: ...

global___GrafanaAssetModel = GrafanaAssetModel

@typing_extensions.final
class GrafanaAssets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSETS_FIELD_NUMBER: builtins.int
    @property
    def assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GrafanaAssetModel]: ...
    def __init__(
        self,
        *,
        assets: collections.abc.Iterable[global___GrafanaAssetModel] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assets", b"assets"]) -> None: ...

global___GrafanaAssets = GrafanaAssets
