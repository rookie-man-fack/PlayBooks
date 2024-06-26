import React from "react";
import {
  ResultTypeType,
  ResultTypeTypes,
} from "../../utils/conditionals/resultTypeOptions.ts";
import Table from "./Table.tsx";
import Timeseries from "./Timeseries.tsx";

type HandleResultTypePropTypes = {
  resultType: ResultTypeType;
  condition: any;
  conditionIndex: number;
};

function HandleResultTypeForm({
  resultType,
  condition,
  conditionIndex,
}: HandleResultTypePropTypes) {
  switch (resultType) {
    case ResultTypeTypes.TABLE:
      return <Table condition={condition} conditionIndex={conditionIndex} />;
    case ResultTypeTypes.TIMESERIES:
      return (
        <Timeseries condition={condition} conditionIndex={conditionIndex} />
      );
    default:
      return (
        <>
          <p className="text-xs font-normal my-2">No Form Configured</p>
        </>
      );
  }
}

export default HandleResultTypeForm;
