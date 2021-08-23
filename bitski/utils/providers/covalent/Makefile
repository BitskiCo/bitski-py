PACKAGE := covalent

repackage-mods: build-pydantic-mods
	mv ${PACKAGE}_fast/src/openapi_server/models ${PACKAGE}/${PACKAGE}_interface/pydantic_models/
	rm -r ${PACKAGE}_fast

build-pydantic-mods: builder
	openapi-generator generate -i ${PACKAGE}_openapi.json -g python-fastapi -o ./${PACKAGE}_fast --api-package ${PACKAGE}_interface --model-name-prefix ${PACKAGE}_

builder: ${PACKAGE}_openapi.json
	openapi-generator generate -i ${PACKAGE}_openapi.json -g python -o ./${PACKAGE} --package-name covalent_interface

clean:
	rm -f hello
	
.PHONY: repackage-mods
