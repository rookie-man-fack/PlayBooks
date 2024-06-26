import { GET_SLACK_ALERT_METRIC } from "../../../../constants/index.ts";
import { sortByKey } from "../../../../utils/sortByKey.ts";
import { apiSlice } from "../../../app/apiSlice.ts";

export const getSlackAlertMetricApi = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getSlackAlertMetric: builder.query<any, any>({
      query: ({ filter_channels, filter_alert_types }) => ({
        url: GET_SLACK_ALERT_METRIC,
        method: "POST",
        body: {
          metric_title: "ALERT_WEEKLY_DISTRIBUTION_BY_ALERT_TITLE",
          metric_name: "ALERT_WEEKLY_DISTRIBUTION_BY_ALERT_TITLE",
          filter_channels: filter_channels.map((e) => e.label),
          filter_alert_types: filter_alert_types.map((e) => e.label),
          meta: {
            time_range: {
              time_geq: Math.round(
                new Date(
                  new Date().getTime() - 6 * 7 * 24 * 60 * 60 * 1000,
                ).getTime() / 1000,
              ),
              time_lt: Math.round(Date.now() / 1000),
            },
          },
        },
      }),
      transformResponse: (response: any) => {
        if (response.data?.users?.length > 0) {
          return sortByKey(response.data.users, "first_name");
        }
        return [];
      },
    }),
  }),
});

export const { useLazyGetSlackAlertMetricQuery } = getSlackAlertMetricApi;
