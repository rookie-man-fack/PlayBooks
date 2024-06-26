import { GET_ASSETS } from "../../../../../constants/index.ts";
import { updateCardById } from "../../../../../utils/execution/updateCardById.ts";
import extractModelOptions from "../../../../../utils/extractModelOptions.ts";
import getCurrentTask from "../../../../../utils/getCurrentTask.ts";
import handleAssets from "../../../../../utils/handleAssets.ts";
import { apiSlice } from "../../../../app/apiSlice.ts";
import { setAssets } from "../../playbookSlice.ts";

export const getAssetApi = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    getAssets: builder.query<any, string>({
      query: (id) => {
        const [task] = getCurrentTask(id);
        return {
          url: GET_ASSETS,
          method: "POST",
          body: {
            connector_id: task?.connectorType,
            type: task?.modelType,
          },
        };
      },
      transformResponse: (response: any, _, arg) => {
        const [task, id] = getCurrentTask(arg);
        const data = response?.assets;
        if (data?.length === 0) return [];
        let connector_type = task.source;
        if (connector_type?.includes("_VPC"))
          connector_type = connector_type.replace("_VPC", "");

        const assets = handleAssets(data, connector_type, arg);
        const modelOptions = extractModelOptions(assets, task);
        updateCardById("modelOptions", modelOptions, id);
        return assets;
      },
      onQueryStarted: async (arg, { dispatch, queryFulfilled }) => {
        try {
          // Wait for the query to complete
          updateCardById("assetsLoading", true, arg);
          const { data } = await queryFulfilled;
          // Dispatch an action to update the global state
          dispatch(setAssets({ assets: data, id: arg }));
        } catch (error) {
          // Handle any errors
          console.log(error);
        } finally {
          updateCardById("assetsLoading", false, arg);
        }
      },
    }),
  }),
});

export const {
  endpoints: { getAssets },
} = getAssetApi;
