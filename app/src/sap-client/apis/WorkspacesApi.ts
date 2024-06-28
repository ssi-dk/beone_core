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
    CreateWorkspace,
    CreateWorkspaceFromJSON,
    CreateWorkspaceToJSON,
    UpdateWorkspace,
    UpdateWorkspaceFromJSON,
    UpdateWorkspaceToJSON,
    Workspace,
    WorkspaceFromJSON,
    WorkspaceToJSON,
    WorkspaceInfo,
    WorkspaceInfoFromJSON,
    WorkspaceInfoToJSON,
} from '../models';

export interface CreateWorkspaceRequest {
    createWorkspace?: CreateWorkspace;
}

export interface DeleteWorkspaceRequest {
    workspaceId: string;
}

export interface DeleteWorkspaceSampleRequest {
    workspaceId: string;
    sampleId: string;
}

export interface GetWorkspaceRequest {
    workspaceId: string;
}

export interface PostWorkspaceRequest {
    workspaceId: string;
    updateWorkspace?: UpdateWorkspace;
}


/**
 */
function createWorkspaceRaw<T>(requestParameters: CreateWorkspaceRequest, requestConfig: runtime.TypedQueryConfig<T, void> = {}): QueryConfig<T> {
    let queryParameters = null;


    const headerParameters : runtime.HttpHeaders = {};

    headerParameters['Content-Type'] = 'application/json';


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
            method: 'POST',
            headers: headerParameters,
        },
        body: queryParameters || CreateWorkspaceToJSON(requestParameters.createWorkspace),
    };

    const { transform: requestTransform } = requestConfig;
    if (requestTransform) {
    }

    return config;
}

/**
*/
export function createWorkspace<T>(requestParameters: CreateWorkspaceRequest, requestConfig?: runtime.TypedQueryConfig<T, void>): QueryConfig<T> {
    return createWorkspaceRaw(requestParameters, requestConfig);
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
 * Delete sample from workspace
 */
function deleteWorkspaceSampleRaw<T>(requestParameters: DeleteWorkspaceSampleRequest, requestConfig: runtime.TypedQueryConfig<T, void> = {}): QueryConfig<T> {
    if (requestParameters.workspaceId === null || requestParameters.workspaceId === undefined) {
        throw new runtime.RequiredError('workspaceId','Required parameter requestParameters.workspaceId was null or undefined when calling deleteWorkspaceSample.');
    }

    if (requestParameters.sampleId === null || requestParameters.sampleId === undefined) {
        throw new runtime.RequiredError('sampleId','Required parameter requestParameters.sampleId was null or undefined when calling deleteWorkspaceSample.');
    }

    let queryParameters = null;


    const headerParameters : runtime.HttpHeaders = {};


    const { meta = {} } = requestConfig;

    meta.authType = ['bearer'];
    const config: QueryConfig<T> = {
        url: `${runtime.Configuration.basePath}/workspace/{workspace_id}/{sample_id}`.replace(`{${"workspace_id"}}`, encodeURIComponent(String(requestParameters.workspaceId))).replace(`{${"sample_id"}}`, encodeURIComponent(String(requestParameters.sampleId))),
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
* Delete sample from workspace
*/
export function deleteWorkspaceSample<T>(requestParameters: DeleteWorkspaceSampleRequest, requestConfig?: runtime.TypedQueryConfig<T, void>): QueryConfig<T> {
    return deleteWorkspaceSampleRaw(requestParameters, requestConfig);
}

/**
 * Get an existing workspace
 */
function getWorkspaceRaw<T>(requestParameters: GetWorkspaceRequest, requestConfig: runtime.TypedQueryConfig<T, WorkspaceInfo> = {}): QueryConfig<T> {
    if (requestParameters.workspaceId === null || requestParameters.workspaceId === undefined) {
        throw new runtime.RequiredError('workspaceId','Required parameter requestParameters.workspaceId was null or undefined when calling getWorkspace.');
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
            method: 'GET',
            headers: headerParameters,
        },
        body: queryParameters,
    };

    const { transform: requestTransform } = requestConfig;
    if (requestTransform) {
        config.transform = (body: ResponseBody, text: ResponseBody) => requestTransform(WorkspaceInfoFromJSON(body), text);
    }

    return config;
}

/**
* Get an existing workspace
*/
export function getWorkspace<T>(requestParameters: GetWorkspaceRequest, requestConfig?: runtime.TypedQueryConfig<T, WorkspaceInfo>): QueryConfig<T> {
    return getWorkspaceRaw(requestParameters, requestConfig);
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

/**
 * Updates an existing workspace
 */
function postWorkspaceRaw<T>(requestParameters: PostWorkspaceRequest, requestConfig: runtime.TypedQueryConfig<T, void> = {}): QueryConfig<T> {
    if (requestParameters.workspaceId === null || requestParameters.workspaceId === undefined) {
        throw new runtime.RequiredError('workspaceId','Required parameter requestParameters.workspaceId was null or undefined when calling postWorkspace.');
    }

    let queryParameters = null;


    const headerParameters : runtime.HttpHeaders = {};

    headerParameters['Content-Type'] = 'application/json';


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
            method: 'POST',
            headers: headerParameters,
        },
        body: queryParameters || UpdateWorkspaceToJSON(requestParameters.updateWorkspace),
    };

    const { transform: requestTransform } = requestConfig;
    if (requestTransform) {
    }

    return config;
}

/**
* Updates an existing workspace
*/
export function postWorkspace<T>(requestParameters: PostWorkspaceRequest, requestConfig?: runtime.TypedQueryConfig<T, void>): QueryConfig<T> {
    return postWorkspaceRaw(requestParameters, requestConfig);
}

