// tslint:disable
/**
 * SAP
 * Sekvensanalyseplatform
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import {
    LimsMetadata,
    LimsMetadataFromJSON,
    LimsMetadataToJSON,
    TbrMetadata,
    TbrMetadataFromJSON,
    TbrMetadataToJSON,
} from './';

/**
 * @type MetadataReloadResponse
 * @export
 */
export type MetadataReloadResponse = LimsMetadata | TbrMetadata;


export function MetadataReloadResponseFromJSON(json: any): MetadataReloadResponse {
  switch (json.institution) {
  default: throw new Error("Unexpected institution value.");
  }
}

export function MetadataReloadResponseToJSON(value?: MetadataReloadResponse): any {
    if (value === undefined) {
        return undefined;
    }

    switch (value.institution) {
    default: throw new Error("Unexpected institution value.");
    }
}

