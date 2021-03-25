// tslint:disable
/**
 * SOFI
 * SOFI Sekvensanalyseplatform
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface BulkUploadRequest
 */
export interface BulkUploadRequest  {
    /**
     * 
     * @type {string}
     * @memberof BulkUploadRequest
     */
    path: string;
    /**
     * 
     * @type {Blob}
     * @memberof BulkUploadRequest
     */
    metadata_tsv: Blob;
}

export function BulkUploadRequestFromJSON(json: any): BulkUploadRequest {
    return {
        'path': json['path'],
        'metadata_tsv': json['metadata_tsv'],
    };
}

export function BulkUploadRequestToJSON(value?: BulkUploadRequest): any {
    if (value === undefined) {
        return undefined;
    }
    return {
        'path': value.path,
        'metadata_tsv': value.metadata_tsv,
    };
}


