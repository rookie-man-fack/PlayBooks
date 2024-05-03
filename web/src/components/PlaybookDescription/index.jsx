import React from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  playbookSelector,
  setPlaybookKey,
} from "../../store/features/playbook/playbookSlice.ts";

function PlaybookDescription() {
  const { description, currentPlaybook } = useSelector(playbookSelector);
  const dispatch = useDispatch();

  const handleDescription = (e) => {
    const value = e.target.value;
    if (currentPlaybook.isPrefetched && !currentPlaybook.isCopied) return;
    dispatch(setPlaybookKey({ key: "description", value: value }));
  };
  return (
    <div>
      <p className="text-sm font-semibold text-gray-500">Description</p>
      <textarea
        placeholder={
          !currentPlaybook.isPrefetched
            ? "Playbook description goes here..."
            : ""
        }
        className="p-1 w-full rounded border text-sm h-32 resize-none"
        onChange={handleDescription}
        disabled={currentPlaybook.isPrefetched && !currentPlaybook.isCopied}
        value={description}
      />
    </div>
  );
}

export default PlaybookDescription;