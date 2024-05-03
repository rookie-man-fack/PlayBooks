import { store } from "../../store/index.ts";
import { changeProgress } from "../../store/features/playbook/playbookSlice.ts";
import { queryForStepTask } from "./queryForStepTask.ts";
import { updateCardByIndex } from "./updateCardByIndex.ts";

export const handleExecute = (step) => {
  const currentStepIndex = store.getState().playbook.currentStepIndex;
  store.dispatch(changeProgress({ index: currentStepIndex, progress: true }));

  updateCardByIndex("outputLoading", true);
  updateCardByIndex("showOutput", true);
  updateCardByIndex("outputError", null);
  updateCardByIndex("output", null);
  updateCardByIndex("showError", false);

  queryForStepTask(step, function (res) {
    if (Object.keys(res ?? {}).length > 0) {
      if (res.err) {
        updateCardByIndex("showOutput", true);
        updateCardByIndex("outputLoading", false);
        return;
      }
      updateCardByIndex("showOutput", true);
      updateCardByIndex("output", res);
      updateCardByIndex("outputLoading", false);
      store.dispatch(
        changeProgress({ index: currentStepIndex, progress: false }),
      );
    } else {
      updateCardByIndex("showError", true);
      updateCardByIndex("showOutput", false);
      updateCardByIndex("outputLoading", false);
    }
  });
};