import React from "react";
import { useSelector } from "react-redux";
import { useRequests } from "redux-query-react";
import { Analysis } from "sap-client";
import DataTable from "app/analysis/data-table/data-table";
import { RootState } from "app/root-reducer";
import { Column } from "react-table";
import RequestPageOfAnalysis from "./analysis-query-configs";

function AnalysisDataTable() {
  const columns = React.useMemo(
    (): Column<Analysis>[] => [
      {
        Header: "Row Index",
        accessor: (row: any, i: number) => i,
      },
      // {
      //  Header: "Run",
      //  columns: [
      {
        Header: "ID",
        accessor: "analysisId",
      },
      {
        Header: "Isolate",
        accessor: "isolateId",
      },
      {
        Header: "Job time",
        accessor: "testTimestamp",
      },
      //  ],
      // },
      // {
      //  Header: "Source",
      //  columns: [
      {
        Header: "Organization",
        accessor: "organization",
      },
      {
        Header: "Date Received",
        accessor: "dateReceived",
      },
      {
        Header: "Project",
        accessor: "project",
      },
      //  ],
      // },
      // {
      //  Header: "Details",
      //  columns: [
      {
        Header: "Agent",
        accessor: "agent",
      },
      {
        Header: "Species",
        accessor: "species",
      },
      {
        Header: "Resfinder Ver.",
        accessor: "resfinderVersion",
      },
      {
        Header: "Serum type",
        accessor: "serumType",
      },
      //   ],
      // },
      // {
      //   Header: "Status",
      //   columns: [
      {
        Header: "Approved",
        accessor: "approved",
      },
      //   ],
      // },
    ],
    []
  );

  const reqs = React.useMemo(
    () =>
      Array.from(Array(5).keys()).map((i) => ({
        ...RequestPageOfAnalysis({ pageSize: 1000 }),
        queryKey: `${i}`,
      })),
    []
  );
  const [{ isPending, isFinished }] = useRequests(reqs);
  // TODO: Figure out how to make this strongly typed
  const data = useSelector<RootState>((s) =>
    Object.values(s.entities.analysis ?? {})
  ) as any;

  return (
    <>
      <DataTable columns={columns} data={data} />
      {isPending && `Fetching... ${data.length}`}
      {isFinished && `Found ${data.length} records.`}
    </>
  );
}

export default AnalysisDataTable;
