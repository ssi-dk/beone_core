import React from "react";
import "@compiled/react";
import { ChakraProvider } from "@chakra-ui/react";
import { Route } from "react-router";
import { CacheSwitch, CacheRoute } from "react-router-cache-route";
import { Authorize } from "auth/authorize";
import appTheme from "app/app.theme";
import { Callback } from "auth/auth-callback";
import { globalCss } from "./app.styles";
import "./i18n";
import AnalysisPage from "./analysis/analysis-page";
import ApprovalHistory from "./approval-history/approval-history";
import ManualUploadPage from "./manual-upload/manual-upload-page";
import GdprPage from "./gdpr/gdpr";
import Tree from "./comparative-analysis/phylo/phylo";
import ComparativeAnalysis from "./comparative-analysis/comparative-analysis";
import "./style-reset.css";
import i18n from "./i18n";

export default function App() {
  return (
    <ChakraProvider theme={appTheme}>
      <CacheSwitch>
        <Route
          path="/manual-upload"
          render={() => (
            <Authorize>
              <ManualUploadPage />
            </Authorize>
          )}
        />
        <Route
          exact
          path="/approval-history"
          render={() => (
            <Authorize>
              <ApprovalHistory />
            </Authorize>
          )}
        />
        <Route
          exact
          path="/gdpr"
          render={() => (
            <Authorize>
              <GdprPage />
            </Authorize>
          )}
        />
        <Route
          exact
          path="/phylo"
          render={() => (
            <Authorize>
              <ComparativeAnalysis />
            </Authorize>
          )}
        />
        <Route
          exact
          path="/callback"
          render={() => <Callback location={window.location} />}
        />
        <CacheRoute
          path="/"
          render={() => (
            <Authorize>
              <AnalysisPage />
            </Authorize>
          )}
        />
      </CacheSwitch>
    </ChakraProvider>
  );
}
