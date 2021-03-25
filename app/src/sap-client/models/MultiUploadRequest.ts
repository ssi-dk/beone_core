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
 * @interface MultiUploadRequest
 */
export interface MultiUploadRequest  {
    /**
     * 
     * @type {Blob}
     * @memberof MultiUploadRequest
     */
    metadata_tsv: Blob;
    /**
     * 
     * @type {Array<Blob>}
     * @memberof MultiUploadRequest
     */
    files: Array<Blob>;
}

export function MultiUploadRequestFromJSON(json: any): MultiUploadRequest {
    return {
        'metadata_tsv': json['metadata_tsv'],
        'files': json['files'],
    };
}

export function MultiUploadRequestToJSON(value?: MultiUploadRequest): any {
    if (value === undefined) {
        return undefined;
    }
    return {
        'metadata_tsv': value.metadata_tsv,
        'files': value.files,
    };
}


