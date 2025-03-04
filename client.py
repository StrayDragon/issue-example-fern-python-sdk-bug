import asyncio
from pathlib import Path
import sys
from sdk import AsyncExampleApi as ErrorAsyncExampleApi
from sdk.client2 import AsyncExampleApi as WorkaroundAsyncExampleApi
from sdk.types.update_document_by_file_request_data import (
    UpdateDocumentByFileRequestData,
)


async def main():
    flag = sys.argv[1] if len(sys.argv) > 1 else 0
    if flag == "0":
        client = ErrorAsyncExampleApi(
            authorization="YOUR_AUTHORIZATION",
            token="test_api_key",
        )
    else:
        client = WorkaroundAsyncExampleApi(
            authorization="YOUR_AUTHORIZATION",
            token="test_api_key",
        )
    resp = await client.update_document_by_file(
        dataset_id="test_dataset_id",
        document_id="test_document_id",
        data=UpdateDocumentByFileRequestData(
            name="test_name",
            indexing_technique="high_quality",
        ),
        file=Path("test_file.txt").read_bytes(),
    )
    print(resp)


asyncio.run(main())
