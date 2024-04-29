import { SOURCES, models } from "../../../constants/index.ts";
import {
  Playbook,
  PlaybookContract,
  PlaybookContractStep,
  PlaybookTask,
  Step,
} from "../../../types.ts";
import { v4 as uuidv4 } from "uuid";

export const getTaskFromStep = (step: Step, i?: number): PlaybookTask => {
  const variables = step.globalVariables?.reduce((acc, curr) => {
    acc[curr.name] = curr.value;
    return acc;
  }, {});
  let task: PlaybookTask = {
    name: step.name ?? uuidv4(),
    id: step.id ?? "0",
    type: "METRIC",
    description: step.description || `Step - ${(i ?? 0) + 1}`,
    notes: step.notes ?? "",
    global_variable_set: variables,
  };

  switch (step.source) {
    case SOURCES.CLOUDWATCH:
      let metric_task;
      if (step.modelType === models.CLOUDWATCH_METRIC) {
        metric_task = {
          source: "CLOUDWATCH",
          cloudwatch_task: {
            type: "METRIC_EXECUTION",
            metric_execution_task: {
              namespace: step.namespaceName ?? step.namespace!,
              metric_name: step.metric!,
              region: step.region!,
              process_function: "timeseries",
              statistic: "Average",
              dimensions: [
                {
                  name: step.dimensionName!,
                  value: step.dimensionValue!,
                },
              ],
            },
          },
        };
      } else {
        metric_task = {
          source: "CLOUDWATCH",
          cloudwatch_task: {
            type: "FILTER_LOG_EVENTS",
            filter_log_events_task: {
              region: step.region!,
              log_group_name: step.logGroup!,
              filter_query: step.cw_log_query!,
            },
          },
        };
      }
      task = {
        ...task,
        type: "METRIC",
        metric_task,
      };
      break;
    case SOURCES.GRAFANA_VPC:
    case SOURCES.GRAFANA:
      const options: any = [];
      if (step.selectedOptions) {
        for (let [key, val] of Object.entries(step.selectedOptions)) {
          options.push({
            name: key,
            value: val,
          });
        }
      }
      task = {
        ...task,
        type: "METRIC",
        metric_task: {
          source: step.source.toUpperCase(),
          grafana_task: {
            type: "PROMQL_METRIC_EXECUTION",
            datasource_uid:
              step.assets.panel_promql_map[0].promql_metrics[0].datasource_uid,
            promql_metric_execution_task: {
              promql_expression: step.grafanaQuery.expression,
              panel_promql_expression: step.grafanaQuery.originalExpression,
              process_function: "timeseries",
              promql_label_option_values: options,
              panel_id: step.panel.panel_id,
              panel_title: step.panel.panel_title,
              dashboard_uid: step.dashboard.id,
              dashboard_title: step.dashboard.label,
            },
          },
        },
      };
      break;
    case SOURCES.CLICKHOUSE:
      task = {
        ...task,
        type: "DATA_FETCH",
        data_fetch_task: {
          source: step.source.toUpperCase(),
          clickhouse_data_fetch_task: {
            database: step.database!,
            query: step.dbQuery!,
          },
        },
      };
      break;
    case SOURCES.POSTGRES:
      task = {
        ...task,
        type: "DATA_FETCH",
        data_fetch_task: {
          source: step.source.toUpperCase(),
          postgres_data_fetch_task: {
            database: step.database!,
            query: step.dbQuery!,
          },
        },
      };
      break;
    case SOURCES.EKS:
      task = {
        ...task,
        type: "DATA_FETCH",
        data_fetch_task: {
          source: step.source.toUpperCase(),
          eks_data_fetch_task: {
            region: step.eksRegion!,
            cluster: step.cluster!,
            command_type: step.command?.type!,
            namespace: step.eksNamespace!,
            description: step.command.description!,
          },
        },
      };
      break;
    case SOURCES.TEXT:
      task = {
        ...task,
        type: "DOCUMENTATION",
        documentation_task: {
          type: "MARKDOWN",
          documentation: step.textNotes!,
        },
      };
      break;
    case SOURCES.NEW_RELIC:
      let new_relic_task = {};
      switch (step.modelType) {
        case models.NEW_RELIC_ENTITY_DASHBOARD:
          new_relic_task = {
            ...new_relic_task,
            type: "ENTITY_DASHBOARD_WIDGET_NRQL_METRIC_EXECUTION",
            entity_dashboard_widget_nrql_metric_execution_task: {
              dashboard_guid: step.dashboard?.id,
              dashboard_name: step.dashboard.label,
              page_guid: step.page.page_guid,
              page_name: step.page.page_name,
              widget_id: step.widget.widget_id,
              widget_title: step.widget.widget_title,
              widget_nrql_expression: step.widget.widget_nrql_expression,
              process_function: "timeseries",
            },
          };
          break;

        case models.NEW_RELIC_ENTITY_APPLICATION:
          new_relic_task = {
            ...new_relic_task,
            type: "ENTITY_APPLICATION_GOLDEN_METRIC_EXECUTION",
            entity_application_golden_metric_execution_task: {
              application_entity_guid: step?.assets?.application_entity_guid,
              application_entity_name: step?.assets?.application_name,
              golden_metric_name: step.golden_metric?.golden_metric_name,
              golden_metric_unit: step.golden_metric?.golden_metric_unit,
              golden_metric_nrql_expression:
                step.golden_metric?.golden_metric_nrql_expression,
              process_function: "timeseries",
            },
          };
          break;

        case models.NEW_RELIC_NRQL:
          new_relic_task = {
            ...new_relic_task,
            type: "NRQL_METRIC_EXECUTION",
            nrql_metric_execution_task: {
              metric_name: step.nrqlData?.metric_name,
              unit: step.nrqlData?.unit,
              nrql_expression: step.nrqlData?.nrql_expression,
              process_function: "timeseries",
            },
          };
          break;
      }
      task = {
        ...task,
        type: "METRIC",
        metric_task: {
          source: step.source,
          new_relic_task: {
            type: "",
            ...new_relic_task,
          },
        },
      };
      break;
    case SOURCES.DATADOG:
      switch (step.modelType) {
        case models.DATADOG:
          task = {
            ...task,
            type: "METRIC",
            metric_task: {
              source: "DATADOG",
              datadog_task: {
                type: "SERVICE_METRIC_EXECUTION",
                service_metric_execution_task: {
                  service_name: step.datadogService?.name,
                  environment_name: step?.datadogEnvironment ?? "",
                  metric: step.datadogMetric ?? "",
                  metric_family: step.datadogMetricFamily ?? "",
                  process_function: "timeseries",
                },
              },
            },
          };

          break;

        case models.DATADOG_QUERY:
          task = {
            ...task,
            type: "METRIC",
            metric_task: {
              source: "DATADOG",
              datadog_task: {
                type: "QUERY_METRIC_EXECUTION",
                query_metric_execution_task: {
                  queries: step.query2
                    ? [step.query1!, step.query2]
                    : [step.query1!],
                  formula: step.formula!,
                  process_function: "timeseries",
                },
              },
            },
          };

          break;
      }
      break;

    default:
      task = {
        ...task,
        type: "DOCUMENTATION",
        documentation_task: {
          type: "MARKDOWN",
          documentation: step.textNotes!,
        },
      };
  }

  return task;
};

export const stepsToPlaybook = (playbookVal: Playbook, steps: Step[]) => {
  const playbookContractSteps: PlaybookContractStep[] = steps.map((step, i) => {
    return {
      name: step.name!,
      description: step.description || `Step - ${(i ?? 0) + 1}`,
      external_links: step.externalLinks ?? [],
      tasks: [getTaskFromStep(step, i)],
    };
  });
  let playbook: PlaybookContract = {
    name: playbookVal.name,
    global_variable_set: playbookVal.globalVariables?.reduce((acc, curr) => {
      acc[curr.name] = curr.value;
      return acc;
    }, {}),
    steps: playbookContractSteps,
  };

  return playbook;
};