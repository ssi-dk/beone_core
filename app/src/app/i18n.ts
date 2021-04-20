import { template } from "@babel/core";
import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import { isTemplateExpression } from "typescript";
import { invertMap } from "utils";

const fieldDisplayNames = {
  da: {
    public: "Acc_nr",
    received_date: "Modtagedato",
    sampling_date: "Prøvetagningsdato",
    institution: "Institution",
    project_title: "Projekt_titel",
    project_number: "Projekt_nr",
    provided_species: "Provided_species",
    animal_species: "Dyreart",
    run_id: "RunID",
    isolate_id: "IsolatID",
    fud_number: "Fud_nr",
    cluster_id: "ClusterID",
    serotype_final: "Serotype_final",
    st: "ST",
    infection_source: "Smittekilde",
    comment_cluster: "Kommentar_cluster",
    comment_general: "Kommentar_generelt",
  },
};

const resources = {
  da: {
    translation: {
      From: "Fra",
      To: "Til",
      Select: "Tilvælg",
      Cancel: "Annullér",
      Return: "Tilbage",
      Found: "Fundet",
      records: "enheder",
      Staging: "Forbereder",
      Approve: "Godkend",
      Reject: "Afvis",
      "Approval submitted": "Godkendelse indsendt",
      "Rejection submitted": "Afvising indsendt",
      "have been submitted for approval.": "er blevet registeret som godkendt.",
      "have been rejected.": "er blevet afvist.",
      MetadataFilter: "Metadata filter",
      AnalysisFilter: "Analyse filter",
      Organisation: "Organisation",
      Project: "Projekt",
      Species: "Dyreart",
      Agens: "Agens",
      Serotype: "Serotype",
      ResfinderVersion: "Resfinder version",
      "Save current view": "Gem nuværende view",
      "Delete current view": "Slet nuværende view",
      "Predefined views": "Prædefinerede views",
      "My views": "Mine views",
      Time: "Tid",
      Sequences: "Sekvenser",
      "Approved by": "Godkendt af",
      "Revoke approval": "Tilbagekald godkendelse",
      "My approval history": "Min godkendelseshistorik",
      "Analysis results": "Analyseresultater",
      approvals: "godkendelser",
      "Sign in failed": "Kunne ikke log på",
      "Error message:": "Fejlbesked:",
      "History for isolate": "Historik for isolat ID:",
      Logout: "Log ud",
      Microbiologist: "Mikrobiolog",
      User: "Bruger",
      Level: "Niveau",
      Update: "Opdater",
      Reload: "Genindlæs",
      Load: "Indlæs",
      Loading: "Indlæser",
      Close: "Luk",
      MetadataReloaded: "Metadata genindlæst",
      IsolateMetadataReloadedFor: "Genindlæst metadata for isolat",
      MetadataNotReloaded: "Metadata ikke genindlæst",
      IsolateMetadataNotReloadedFor:
        "Grundet fejl er metadata ikke genindlæst for isolat",

      // field name translations
      ...fieldDisplayNames.da,
    },
  },
};

i18n
  .use(initReactI18next) // passes i18n down to react-i18next
  .init({
    resources,
    lng: "da",

    keySeparator: false, // we do not use keys in form messages.welcome

    interpolation: {
      escapeValue: false, // react already safe from xss
    },
  });

/**
 * Get the display name of a field given its internal name
 * @param internalName the internal name of the field
 * @param lang i18n lng code to translate displayName to. Defaults to current language
 */
export const getFieldDisplayName = (
  internalName: string,
  lang?: string | undefined
) => {
  const lng = lang ?? i18n.language;
  return fieldDisplayNames[lng][internalName];
};

const flippedFieldMap = Object.keys(fieldDisplayNames)
  .map((x) => ({ key: x, value: invertMap(fieldDisplayNames[x], true) }))
  .reduce((obj, item) => (obj[item.key] = item.value) && obj, {});

/**
 * Get the internal name of a field given its displayName
 * @param displayName the display name of the field. Case insensitive
 * @param lang i18n lng code to translate displayName from. Defaults to current language
 */
export const getFieldInternalName = (
  displayName: string,
  lang?: string | undefined
) => {
  const lng = lang ?? i18n.language;
  return flippedFieldMap[lng][displayName.toLocaleLowerCase()];
};

export default i18n;
