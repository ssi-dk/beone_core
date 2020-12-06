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

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface AnalysisResult
 */
export interface AnalysisResult  {
    /**
     * 
     * @type {string}
     * @memberof AnalysisResult
     */
    id: string;
    /**
     * 
     * @type {string}
     * @memberof AnalysisResult
     */
    isolateId: string;
    /**
     * 
     * @type {number}
     * @memberof AnalysisResult
     */
    qCProvidedSpecies?: number;
    /**
     * 
     * @type {number}
     * @memberof AnalysisResult
     */
    qCGenome1x?: number;
    /**
     * 
     * @type {number}
     * @memberof AnalysisResult
     */
    qCGenome10x?: number;
    /**
     * 
     * @type {number}
     * @memberof AnalysisResult
     */
    qCGsizeDiff1x10?: number;
    /**
     * 
     * @type {number}
     * @memberof AnalysisResult
     */
    qCAvgCoverage?: number;
}

export function AnalysisResultFromJSON(json: any): AnalysisResult {
    return {
        'id': json['_id'],
        'isolateId': json['isolateId'],
        'qCProvidedSpecies': !exists(json, 'QC_provided_species') ? undefined : json['QC_provided_species'],
        'qCGenome1x': !exists(json, 'QC_genome1x') ? undefined : json['QC_genome1x'],
        'qCGenome10x': !exists(json, 'QC_genome10x') ? undefined : json['QC_genome10x'],
        'qCGsizeDiff1x10': !exists(json, 'QC_Gsize_diff1x10') ? undefined : json['QC_Gsize_diff1x10'],
        'qCAvgCoverage': !exists(json, 'QC_Avg_coverage') ? undefined : json['QC_Avg_coverage'],
    };
}

export function AnalysisResultToJSON(value?: AnalysisResult): any {
    if (value === undefined) {
        return undefined;
    }
    return {
        '_id': value.id,
        'isolateId': value.isolateId,
        'QC_provided_species': value.qCProvidedSpecies,
        'QC_genome1x': value.qCGenome1x,
        'QC_genome10x': value.qCGenome10x,
        'QC_Gsize_diff1x10': value.qCGsizeDiff1x10,
        'QC_Avg_coverage': value.qCAvgCoverage,
    };
}


