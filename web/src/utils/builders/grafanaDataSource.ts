import {
  setDataSource,
  setGrafanaExpression,
  setGrafanaQuery,
  updateStep,
} from "../../store/features/playbook/playbookSlice.ts";
import { store } from "../../store/index.ts";
import { OptionType } from "../playbooksData.ts";

export const grafanaDataSourceBuilder = (task, index, options: any) => {
  return {
    builder: [
      [
        {
          key: "datasource",
          label: "Data Source",
          type: OptionType.OPTIONS,
          options: options?.map((e) => {
            return {
              id: e.datasource_uid,
              label: e.datasource_name,
            };
          }),
          handleChange: (_, val) => {
            store.dispatch(setDataSource({ index, datasource: val }));
            if (!task?.grafanaQuery?.expression) {
              store.dispatch(
                setGrafanaQuery({
                  index,
                  query: {expression: ''}
                }),
              );
            }
          },
          selected: task.datasource?.id,
        }
      ],
      [
        {
          label: "PromQL",
          type: OptionType.MULTILINE,
          value: task?.grafanaQuery?.expression ? task?.grafanaQuery?.expression : '',
          handleChange: (e) => {
            store.dispatch(
              setGrafanaExpression({ index, expression: e.target.value }),
            );
          },
          condition: task?.grafanaQuery,
        },
      ],
    ],
  };
};