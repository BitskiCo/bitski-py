PACKAGE := rarible
LANGUAGE := python

repackage-mods: build-pydantic-mods
	mkdir -p ${PACKAGE}/${PACKAGE}_interface/pydantic_models/ 
	mv ${PACKAGE}_fast/src/openapi_server/models/* ${PACKAGE}/${PACKAGE}_interface/pydantic_models/
	rm -r ${PACKAGE}_fast

build-pydantic-mods: builder
	openapi-generator generate -i ${PACKAGE}_openapi.yaml -g python-fastapi -o ./${PACKAGE}_fast --api-package ${PACKAGE}_interface

builder: ${PACKAGE}_openapi.yaml
	openapi-generator generate -i ${PACKAGE}_openapi.yaml -g ${LANGUAGE} -o ./${PACKAGE} --package-name ${PACKAGE}_interface

install:
    ( \
       source path/to/virtualenv/bin/activate; \
       
	   pip install -r requirements.txt; \

    )

clean:
	rm -f ${PACKAGE}

.PHONY: repackage-mods
