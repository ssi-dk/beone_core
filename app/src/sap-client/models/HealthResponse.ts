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
import {
    Exception,
    ExceptionFromJSON,
    ExceptionToJSON,
    HealthStatus,
    HealthStatusFromJSON,
    HealthStatusToJSON,
} from './';

/**
 * 
 * @export
 * @interface HealthResponse
 */
export interface HealthResponse  {
    /**
     * 
     * @type {object}
     * @memberof HealthResponse
     */
    data?: object;
    /**
     * 
     * @type {string}
     * @memberof HealthResponse
     */
    description: string;
    /**
     * 
     * @type {Exception}
     * @memberof HealthResponse
     */
    exception?: Exception;
    /**
     * 
     * @type {HealthStatus}
     * @memberof HealthResponse
     */
    status: HealthStatus;
}

export function HealthResponseFromJSON(json: any): HealthResponse {
    return {
        'data': !exists(json, 'data') ? undefined : json['data'],
        'description': json['description'],
        'exception': !exists(json, 'exception') ? undefined : ExceptionFromJSON(json['exception']),
        'status': HealthStatusFromJSON(json['status']),
    };
}

export function HealthResponseToJSON(value?: HealthResponse): any {
    if (value === undefined) {
        return undefined;
    }
    return {
        'data': value.data,
        'description': value.description,
        'exception': ExceptionToJSON(value.exception),
        'status': HealthStatusToJSON(value.status),
    };
}


