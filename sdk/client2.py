# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import ExampleApiEnvironment
import httpx
from .core.client_wrapper import SyncClientWrapper
from .types.update_document_by_file_request_data import UpdateDocumentByFileRequestData
from . import core
from .core.request_options import RequestOptions
from .types.update_document_by_file_response import UpdateDocumentByFileResponse
from .core.jsonable_encoder import jsonable_encoder
from .core.pydantic_utilities import parse_obj_as
from .errors.bad_request_error import BadRequestError
from .errors.unauthorized_error import UnauthorizedError
from json.decoder import JSONDecodeError
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ExampleApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : ExampleApiEnvironment
        The environment to use for requests from the client. from .environment import ExampleApiEnvironment



        Defaults to ExampleApiEnvironment.DEFAULT



    authorization : str
    token : typing.Union[str, typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from example import ExampleApi

    client = ExampleApi(
        authorization="YOUR_AUTHORIZATION",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ExampleApiEnvironment = ExampleApiEnvironment.DEFAULT,
        authorization: str,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else None
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            authorization=authorization,
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(
                timeout=_defaulted_timeout, follow_redirects=follow_redirects
            )
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )

    def update_document_by_file(
        self,
        dataset_id: str,
        document_id: str,
        *,
        data: UpdateDocumentByFileRequestData,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateDocumentByFileResponse:
        """
        Updates a document in a dataset by uploading a file

        Parameters
        ----------
        dataset_id : str
            ID of the dataset

        document_id : str
            ID of the document

        data : UpdateDocumentByFileRequestData
            Document configuration JSON as string

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateDocumentByFileResponse
            Document updated successfully

        Examples
        --------
        from example import ExampleApi, UpdateDocumentByFileRequestData

        client = ExampleApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.update_document_by_file(
            dataset_id="dataset_id",
            document_id="document_id",
            data=UpdateDocumentByFileRequestData(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/datasets/{jsonable_encoder(dataset_id)}/documents/{jsonable_encoder(document_id)}/update-by-file",
            method="POST",
            data={
                "data": data.model_dump_json(),
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    UpdateDocumentByFileResponse,
                    parse_obj_as(
                        type_=UpdateDocumentByFileResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncExampleApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : ExampleApiEnvironment
        The environment to use for requests from the client. from .environment import ExampleApiEnvironment



        Defaults to ExampleApiEnvironment.DEFAULT



    authorization : str
    token : typing.Union[str, typing.Callable[[], str]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from example import AsyncExampleApi

    client = AsyncExampleApi(
        authorization="YOUR_AUTHORIZATION",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: ExampleApiEnvironment = ExampleApiEnvironment.DEFAULT,
        authorization: str,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else None
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            authorization=authorization,
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(
                timeout=_defaulted_timeout, follow_redirects=follow_redirects
            )
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )

    async def update_document_by_file(
        self,
        dataset_id: str,
        document_id: str,
        *,
        data: UpdateDocumentByFileRequestData,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateDocumentByFileResponse:
        """
        Updates a document in a dataset by uploading a file

        Parameters
        ----------
        dataset_id : str
            ID of the dataset

        document_id : str
            ID of the document

        data : UpdateDocumentByFileRequestData
            Document configuration JSON as string

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateDocumentByFileResponse
            Document updated successfully

        Examples
        --------
        import asyncio

        from example import AsyncExampleApi, UpdateDocumentByFileRequestData

        client = AsyncExampleApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.update_document_by_file(
                dataset_id="dataset_id",
                document_id="document_id",
                data=UpdateDocumentByFileRequestData(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/datasets/{jsonable_encoder(dataset_id)}/documents/{jsonable_encoder(document_id)}/update-by-file",
            method="POST",
            data={
                "data": data.model_dump_json(),
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    UpdateDocumentByFileResponse,
                    parse_obj_as(
                        type_=UpdateDocumentByFileResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: ExampleApiEnvironment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception(
            "Please pass in either base_url or environment to construct the client"
        )
