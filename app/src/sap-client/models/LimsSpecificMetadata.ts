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
 * @interface LimsSpecificMetadata
 */
export interface LimsSpecificMetadata  {
    /**
     * 
     * @type {string}
     * @memberof LimsSpecificMetadata
     */
    chr_number?: string;
    /**
     * 
     * @type {string}
     * @memberof LimsSpecificMetadata
     */
    cvr_number?: string;
    /**
     * 
     * @type {string}
     * @memberof LimsSpecificMetadata
     */
    aut_number?: string;
    /**
     * 
     * @type {string}
     * @memberof LimsSpecificMetadata
     */
    product_type?: string;
    /**
     * 
     * @type {string}
     * @memberof LimsSpecificMetadata
     */
    product?: string;
    /**
     * 
     * @type {string}
     * @memberof LimsSpecificMetadata
     */
    origin_country?: string;
    /**
     * 
     * @type {string}
     * @memberof LimsSpecificMetadata
     */
    animal_species?: string;
    /**
     * 
     * @type {string}
     * @memberof LimsSpecificMetadata
     */
    sample_info?: string;
}

export function LimsSpecificMetadataFromJSON(json: any): LimsSpecificMetadata {
    return {
        'chr_number': !exists(json, 'chr_number') ? undefined : json['chr_number'],
        'cvr_number': !exists(json, 'cvr_number') ? undefined : json['cvr_number'],
        'aut_number': !exists(json, 'aut_number') ? undefined : json['aut_number'],
        'product_type': !exists(json, 'product_type') ? undefined : json['product_type'],
        'product': !exists(json, 'product') ? undefined : json['product'],
        'origin_country': !exists(json, 'origin_country') ? undefined : json['origin_country'],
        'animal_species': !exists(json, 'animal_species') ? undefined : json['animal_species'],
        'sample_info': !exists(json, 'sample_info') ? undefined : json['sample_info'],
    };
}

export function LimsSpecificMetadataToJSON(value?: LimsSpecificMetadata): any {
    if (value === undefined) {
        return undefined;
    }
    return {
        'chr_number': value.chr_number,
        'cvr_number': value.cvr_number,
        'aut_number': value.aut_number,
        'product_type': value.product_type,
        'product': value.product,
        'origin_country': value.origin_country,
        'animal_species': value.animal_species,
        'sample_info': value.sample_info,
    };
}


