/* eslint-disable react-hooks/exhaustive-deps */
import ReactFlow, {
  Background,
  Controls,
  useNodesState,
  useEdgesState,
  addEdge,
} from "reactflow";
import "reactflow/dist/style.css";
import { useDispatch } from "react-redux";
import { addParentId } from "../../../store/features/playbook/playbookSlice.ts";
import { useCallback, useEffect } from "react";
import CustomNode from "./CustomNode.jsx";
import { useReactFlow } from "reactflow";
import ParentNode from "./ParentNode.jsx";
import CustomEdge from "./CustomEdge.jsx";
import useDimensions from "../../../hooks/useDimensions.ts";
import useGraphDimensions from "../../../hooks/useGraphDimensions.ts";

const fitViewOptions = {
  maxZoom: 0.75,
  duration: 500,
};

const nodeTypes = {
  custom: CustomNode,
  parent: ParentNode,
};

const edgeTypes = {
  custom: CustomEdge,
};

const CreateFlow = () => {
  const reactFlowInstance = useReactFlow();
  const [graphRef, { width, height }] = useDimensions();
  const { graphData, dagreData } = useGraphDimensions(
    width,
    height,
    reactFlowInstance,
  );
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState(graphData.edges ?? []);
  const dispatch = useDispatch();

  const onConnect = useCallback(
    ({ source, target }) => {
      return setEdges((eds) =>
        nodes
          .filter((node) => node.id === source || node.selected)
          .reduce((eds, node) => {
            const stepId = target.split("-")[1];
            const parentId = node.id.split("-")[1];
            dispatch(addParentId({ id: stepId, parentId }));
            return addEdge({ source: node.id, target }, eds);
          }, eds),
      );
    },
    [nodes],
  );

  useEffect(() => {
    if (dagreData?.nodes?.length > 0) {
      setNodes(
        dagreData?.nodes?.map((node) => ({
          ...node,
          data: {
            ...node.data,
          },
        })),
      );
    }
    if (dagreData?.edges?.length > 0) {
      setEdges(dagreData.edges);
    }
  }, [dagreData]);

  return (
    <div ref={graphRef} className="h-full w-full">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        minZoom={-Infinity}
        fitView
        maxZoom={0.75}
        fitViewOptions={fitViewOptions}
        onConnect={onConnect}
        className="bg-gray-50">
        <Controls />
        <Background variant="dots" gap={12} size={1} />
      </ReactFlow>
    </div>
  );
};

export default CreateFlow;
