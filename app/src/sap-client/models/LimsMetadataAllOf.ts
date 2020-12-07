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

import { exists, mapValues } from "../runtime";
/**
 *
 * @export
 * @interface LimsMetadataAllOf
 */
export interface LimsMetadataAllOf {
  /**
   *
   * @type {number}
   * @memberof LimsMetadataAllOf
   */
  chr_number?: number;
  /**
   *
   * @type {string}
   * @memberof LimsMetadataAllOf
   */
  aut_number?: string;
  /**
   *
   * @type {string}
   * @memberof LimsMetadataAllOf
   */
  product_type?: string;
  /**
   *
   * @type {string}
   * @memberof LimsMetadataAllOf
   */
  product?: string;
  /**
   *
   * @type {string}
   * @memberof LimsMetadataAllOf
   */
  origin_country?: string;
  /**
   *
   * @type {string}
   * @memberof LimsMetadataAllOf
   */
  animal_species?: string;
  /**
   *
   * @type {string}
   * @memberof LimsMetadataAllOf
   */
  sample_info?: string;
}

export function LimsMetadataAllOfFromJSON(json: any): LimsMetadataAllOf {
  return {
    chr_number: !exists(json, "chr_number") ? undefined : json["chr_number"],
    aut_number: !exists(json, "aut_number") ? undefined : json["aut_number"],
    product_type: !exists(json, "product_type")
      ? undefined
      : json["product_type"],
    product: !exists(json, "product") ? undefined : json["product"],
    origin_country: !exists(json, "origin_country")
      ? undefined
      : json["origin_country"],
    animal_species: !exists(json, "animal_species")
      ? undefined
      : json["animal_species"],
    sample_info: !exists(json, "sample_info") ? undefined : json["sample_info"],
  };
}

export function LimsMetadataAllOfToJSON(value?: LimsMetadataAllOf): any {
  if (value === undefined) {
    return undefined;
  }
  return {
    chr_number: value.chr_number,
    aut_number: value.aut_number,
    product_type: value.product_type,
    product: value.product,
    origin_country: value.origin_country,
    animal_species: value.animal_species,
    sample_info: value.sample_info,
  };
}
