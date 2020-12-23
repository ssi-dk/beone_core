SHELL := /bin/bash

mkfile_u := $(shell id -u)
mkfile_g := $(shell id -g)
mkfile_user := $(mkfile_u):$(mkfile_g)
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(subst /Makefile,,$(mkfile_path))

.PHONY: all clean test

all: clean build

clean:
	rm -rf ${mkfile_dir}/bifrost/bifrost_db/data/db/
	rm -rf ${mkfile_dir}/web/src/SAP/generated/
	rm -rf ${mkfile_dir}/sap_tbr_integration/DG.SAP.TBRIntegration/bin/
	rm -rf ${mkfile_dir}/sap_tbr_integration/DG.SAP.TBRIntegration/obj/
	docker-compose rm -vf

${mkfile_dir}/app/src/sap-client : ${mkfile_dir}/openapi_specs/SAP/SAP.yaml
	# Generate web app client
	rm -rf "${mkfile_dir}/app/sap-client/src"
	rm -rf "${mkfile_dir}/app/sap-client/dist"
	docker run --rm -v "${mkfile_dir}:/mnt" \
		--user ${mkfile_user} \
		"openapitools/openapi-generator:cli-v4.3.0" \
		generate \
		-i "/mnt/openapi_specs/SAP/SAP.yaml" \
		--additional-properties=modelPropertyNaming=original,enumPropertyNaming=original \
		-g typescript-redux-query \
		-o /mnt/app/src/sap-client
	cp -r "${mkfile_dir}/app/src/sap-client/src/"* "${mkfile_dir}/app/src/sap-client"
	rm -rf "${mkfile_dir}/app/src/sap-client/src/"

${mkfile_dir}/web/src/SAP/generated : ${mkfile_dir}/openapi_specs/SAP/SAP.yaml
	# Generate flask api
	docker run --rm -v "${mkfile_dir}:/mnt" \
		--user ${mkfile_user} \
		"openapitools/openapi-generator:cli-v4.3.0" \
		generate \
		-i "/mnt/openapi_specs/SAP/SAP.yaml" \
		-g python-flask \
		-o "/mnt/web/src/SAP" \
		-t "/mnt/openapi_specs/SAP/templates" \
		-c "/mnt/openapi_specs/SAP/SAP-config.yaml"
	rm -rf "${mkfile_dir}/web/src/SAP/generated"
	mv "${mkfile_dir}/web/src/SAP/web/src/SAP/generated" "${mkfile_dir}/web/src/SAP/generated"

${mkfile_dir}/web/src/services/lims/openapi : ${mkfile_dir}/openapi_specs/lims.v1.yaml
	# Generate LIMS client for flask api
	rm -rf ${mkfile_dir}/web/src/services/lims/openapi
	docker run --rm --user ${mkfile_user} -v "${mkfile_dir}:/local" openapitools/openapi-generator-cli generate \
		-i /local/openapi_specs/lims.v1.yaml \
		-g python \
		-o /local \
		--additional-properties packageName=web.src.services.lims.openapi \
		--additional-properties generateSourceCodeOnly=true \
		--global-property apiTests=false,apiDocs=false \
		--global-property modelTests=false,modelDocs=false

${mkfile_dir}/app/node_modules/ : ${mkfile_dir}/app/package.json
	pushd {mkfile_dir}/app && yarn install

build: ${mkfile_dir}/app/src/sap-client ${mkfile_dir}/web/src/SAP/generated ${mkfile_dir}/web/src/services/lims/openapi
	CURRENT_UID=${mkfile_user} docker-compose build --no-cache

run: ${mkfile_dir}/app/src/sap-client ${mkfile_dir}/web/src/SAP/generated ${mkfile_dir}/web/src/services/lims/openapi ${mkfile_dir}/app/node_modules/
	CURRENT_UID=${mkfile_user} docker-compose up --build
