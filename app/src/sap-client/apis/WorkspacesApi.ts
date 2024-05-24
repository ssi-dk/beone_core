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


import { HttpMethods, QueryConfig, ResponseBody, ResponseText } from 'redux-query';
import * as runtime from '../runtime';
import {
    Workspace,
    WorkspaceFromJSON,
    WorkspaceToJSON,
} from '../models';

export interface DeleteWorkspaceRequest {
    workspaceId: string;
}


/**
 * Delete an existing workspace
 */
function deleteWorkspaceRaw<T>(requestParameters: DeleteWorkspaceRequest, requestConfig: runtime.TypedQueryConfig<T, void> = {}): QueryConfig<T> {
    if (requestParameters.workspaceId === null || requestParameters.workspaceId === undefined) {
        throw new runtime.RequiredError('workspaceId','Required parameter requestParameters.workspaceId was null or undefined when calling deleteWorkspace.');
    }

    let queryParameters = null;


    const headerParameters : runtime.HttpHeaders = {};


    const { meta = {} } = requestConfig;

    meta.authType = ['bearer'];
    const config: QueryConfig<T> = {
        url: `${runtime.Configuration.basePath}/workspaces/{workspace_id}`.replace(`{${"workspace_id"}}`, encodeURIComponent(String(requestParameters.workspaceId))),
        meta,
        update: requestConfig.update,
        queryKey: requestConfig.queryKey,
        optimisticUpdate: requestConfig.optimisticUpdate,
        force: requestConfig.force,
        rollback: requestConfig.rollback,
        options: {
            method: 'DELETE',
            headers: headerParameters,
        },
        body: queryParameters,
    };

    const { transform: requestTransform } = requestConfig;
    if (requestTransform) {
    }

    return config;
}

/**
* Delete an existing workspace
*/
export function deleteWorkspace<T>(requestParameters: DeleteWorkspaceRequest, requestConfig?: runtime.TypedQueryConfig<T, void>): QueryConfig<T> {
    return deleteWorkspaceRaw(requestParameters, requestConfig);
}

/**
 * Gets workspaces
 */
function getWorkspacesRaw<T>( requestConfig: runtime.TypedQueryConfig<T, Array<Workspace>> = {}): QueryConfig<T> {
    let queryParameters = null;


    const headerParameters : runtime.HttpHeaders = {};


    const { meta = {} } = requestConfig;

    meta.authType = ['bearer'];
    const config: QueryConfig<T> = {
        url: `${runtime.Configuration.basePath}/workspaces`,
        meta,
        update: requestConfig.update,
        queryKey: requestConfig.queryKey,
        optimisticUpdate: requestConfig.optimisticUpdate,
        force: requestConfig.force,
        rollback: requestConfig.rollback,
        options: {
            method: 'GET',
            headers: headerParameters,
        },
        body: queryParameters,
    };

    const { transform: requestTransform } = requestConfig;
    if (requestTransform) {
        config.transform = (body: ResponseBody, text: ResponseBody) => requestTransform(body.map(WorkspaceFromJSON), text);
    }

    return config;
}

/**
* Gets workspaces
*/
export function getWorkspaces<T>( requestConfig?: runtime.TypedQueryConfig<T, Array<Workspace>>): QueryConfig<T> {
    return getWorkspacesRaw( requestConfig);
}

