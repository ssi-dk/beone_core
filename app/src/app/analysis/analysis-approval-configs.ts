import {
  createApproval,
  ApprovalRequest,
  Approval,
  CancelApprovalRequest,
  cancelApproval,
  getApprovals,
  ApprovalStatus,
  ApprovalAllOfStatusEnum,
  fullApprovalMatrix,
} from "sap-client";
import { getUrl } from "service";

export type ApprovalSlice = {
  approvals: Array<Approval>;
};

const sendJudgement = (params: ApprovalRequest, judgement: ApprovalStatus) => {
  const clone = JSON.parse(JSON.stringify(params));
  const keys = Object.keys(clone.matrix);
  // eslint-disable-next-line
  for (const k of keys) {
    // eslint-disable-next-line
    for (const f of Object.keys(clone.matrix[k])) {
      if (!clone.matrix[k][f]) {
        // remove any negatives that showed up due to toggle on/off
        delete clone.matrix[k][f];
      }
      clone.matrix[k][f] = judgement;
    }
  }
  // use generated api client as base
  const base = createApproval<ApprovalSlice>({ body: clone });
  // template the full path for the url
  base.url = getUrl(base.url);
  // define a transform for normalizing the data into our desired state
  base.transform = (response: Approval) => ({
    approvals: [response],
  });
  // define the update strategy for our state
  base.update = {
    approvals: (oldValue, newValue) => [...newValue, ...(oldValue || [])],
  };
  return base;
};

export const sendApproval = (params: ApprovalRequest) => sendJudgement(params, ApprovalStatus.approved);

export const sendRejection = (params: ApprovalRequest) => sendJudgement(params, ApprovalStatus.rejected);

export const revokeApproval = (params: CancelApprovalRequest) => {
  // use generated api client as base
  const base = cancelApproval<ApprovalSlice>(params);
  // template the full path for the url
  base.url = getUrl(base.url);
  // define the update strategy for our state
  base.update = {
    approvals: (oldValue) => {
      const newValue = JSON.parse(JSON.stringify(oldValue));
      const modded = newValue.filter(x => x.id === params.approvalId)[0];
      modded.status = ApprovalAllOfStatusEnum.cancelled
      return newValue;
    }
  };
  return base;
};

type ApprovalMatrixSlice = { approvalMatrix: ApprovalMatrix };
type ApprovalMatrix = {[K: string]: {[K: string]: ApprovalStatus}}

export const fetchApprovalMatrix = () => {
  const base = fullApprovalMatrix<ApprovalMatrixSlice>();

  base.url = getUrl(base.url);

  base.transform = (response: ApprovalMatrix) => ({ approvalMatrix: response });

  base.update = {
    approvalMatrix: (_, newValue) => newValue,
  };
  return base;
}; 

export const fetchApprovals = () => {
  const base = getApprovals<ApprovalSlice>();

  base.url = getUrl(base.url);

  base.transform = (response: Array<Approval>) => ({
    approvals: response,
  });

  base.update = {
    approvals: (_, newValue) => newValue,
  };
  return base;
};
