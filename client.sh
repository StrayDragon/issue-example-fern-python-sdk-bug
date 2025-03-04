#!/bin/bash

curl --location --request POST 'http://127.0.0.1:5000/v1/datasets/test_dataset_id/documents/test_document_id/update-by-file' \
--header 'Authorization: Bearer test_api_key' \
--form 'data={"name":"Dify","indexing_technique":"high_quality","process_rule":{"rules":{"pre_processing_rules":[{"id":"remove_extra_spaces","enabled":true},{"id":"remove_urls_emails","enabled":true}],"segmentation":{"separator":"###","max_tokens":500}},"mode":"custom"}}' \
--form 'file=@"test_file.txt"'
