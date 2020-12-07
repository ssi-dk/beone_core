import React, { useState } from "react";
import {
  Box,
  Flex,
  Button,
  useToast,
  Text,
  Heading,
  Grid,
} from "@chakra-ui/react";
import {
  CheckIcon,
  DeleteIcon,
  DragHandleIcon,
  NotAllowedIcon,
} from "@chakra-ui/icons";
import { Approval } from "sap-client";
import { useMutation, useRequest } from "redux-query-react";
import { useSelector } from "react-redux";
import { useTranslation } from "react-i18next";
import { RootState } from "app/root-reducer";
import {
  revokeApproval,
  fetchApprovals,
} from "app/analysis/analysis-approval-configs";
import AnalysisHeader from "app/analysis/header/analysis-header";

export default function ApprovalHistory() {
  const [historyLoadState] = useRequest(fetchApprovals());

  // TODO: Figure out how to make this strongly typed
  const approvalHistory = useSelector<RootState>((s) =>
    Object.values(s.entities.approvals ?? {})
  ) as Approval[];

  const { t } = useTranslation();
  const toast = useToast();

  const [revocationLoadState, doRevoke] = useMutation((id: string) =>
    revokeApproval({ id })
  );

  const [needsNotify, setNeedsNotify] = useState(true);

  const revokeItem = React.useCallback(
    (id: string) => {
      setNeedsNotify(true);
      doRevoke(id);
    },
    [doRevoke, setNeedsNotify]
  );

  // Display approval toasts
  React.useMemo(() => {
    if (
      needsNotify &&
      revocationLoadState.status >= 200 &&
      revocationLoadState.status < 300 &&
      !revocationLoadState.isPending
    ) {
      toast({
        title: t("Approval undone"),
        description: `${t("Approval was successfully revoked.")}`,
        status: "info",
        duration: null,
        isClosable: true,
      });
      setNeedsNotify(false);
    }
  }, [t, revocationLoadState, toast, needsNotify, setNeedsNotify]);

  return (
    <Box w="100%">
      <AnalysisHeader hideSearch hideSelector />
      <Flex mt={5}>
        <Box minW="300px" pr={5} />
        <Box borderWidth="1px" rounded="md" overflowX="auto" width="80%">
          <Heading margin="20px">{`${t("My approval history")}`}</Heading>
          <Box margin="4px" />
          {approvalHistory &&
            approvalHistory.map((h) => {
              return (
                <Grid padding="20px" templateColumns="repeat(5, 1fr)" gap={6}>
                  <Text width="100%">{h.id}</Text>
                  <Text>{h.timestamp}</Text>
                  <Text>{h.approver}</Text>
                  <Text>{h.status}</Text>
                  <Button
                    leftIcon={<DeleteIcon />}
                    onClick={() => revokeItem(h.id)}
                  >
                    {`${t("Revoke approval")}`}
                  </Button>
                </Grid>
              );
            })}
          {historyLoadState.isPending && `${t("Fetching...")}`}
          {historyLoadState.isFinished &&
            `${t("Found")} ${approvalHistory.length} ${t("approvals")}.`}
        </Box>
      </Flex>
    </Box>
  );
}
