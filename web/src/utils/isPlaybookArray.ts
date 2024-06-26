import { PlaybookTask } from "../types";

const taskTypes = ["METRIC", "DATA_FETCH", "ACTION"];

export function isPlaybookTaskArray(value: any): value is PlaybookTask[] {
  return (
    Array.isArray(value) &&
    value.every((task) => task && taskTypes.includes(task.type))
  );
}
