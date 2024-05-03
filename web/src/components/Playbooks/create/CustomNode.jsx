import React from "react";
import { Handle, Position } from "reactflow";
import { useDispatch, useSelector } from "react-redux";
import {
  playbookSelector,
  setCurrentStepIndex,
} from "../../../store/features/playbook/playbookSlice.ts";
import { cardsData } from "../../../utils/cardsData.js";
import { CircularProgress } from "@mui/material";
import { CheckCircleOutline, ErrorOutline } from "@mui/icons-material";

export default function CustomNode({ data }) {
  const dispatch = useDispatch();
  const { currentStepIndex } = useSelector(playbookSelector);

  const handleClick = () => {
    dispatch(setCurrentStepIndex(data.index));
  };

  return (
    <div
      className={`${
        currentStepIndex === data.index.toString() ? "shadow-violet-500" : ""
      } px-4 py-2 shadow-md rounded-md bg-white border-2 border-stone-400 w-[200px] h-48 cursor-pointer transition-all hover:shadow-violet-500`}
      onClick={handleClick}>
      <div className="">
        {(data.step.outputLoading || data.step.inprogress) && (
          <CircularProgress size={20} />
        )}
        {(data.step.outputError || data.step.showError) && (
          <ErrorOutline color="error" size={20} />
        )}
        {!data.step.outputError &&
          !data.step.outputLoading &&
          data.step.showOutput &&
          data.step.output &&
          !data.step.showError && (
            <CheckCircleOutline color="success" size={20} />
          )}
      </div>

      <div className="flex flex-col items-center gap-4">
        {data?.step?.source && (
          <img
            className="w-10 h-10"
            src={
              cardsData.find(
                (e) => e.enum === data?.step?.source.replace("_VPC", ""),
              )?.url ?? ""
            }
            alt="logo"
          />
        )}
        <p className="text-lg font-bold text-center z-10 break-word">
          {data?.step?.description ||
            data?.step?.selectedSource ||
            `Step - ${data?.index + 1}`}
        </p>
      </div>
      <Handle
        type="target"
        position={Position.Top}
        className="!bg-violet-500"
      />
    </div>
  );
}