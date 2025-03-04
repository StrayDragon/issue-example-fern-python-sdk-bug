# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .update_document_by_file_response_document_data_source_info import (
    UpdateDocumentByFileResponseDocumentDataSourceInfo,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class UpdateDocumentByFileResponseDocument(UniversalBaseModel):
    id: typing.Optional[str] = None
    position: typing.Optional[int] = None
    data_source_type: typing.Optional[str] = None
    data_source_info: typing.Optional[
        UpdateDocumentByFileResponseDocumentDataSourceInfo
    ] = None
    dataset_process_rule_id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    created_from: typing.Optional[str] = None
    created_by: typing.Optional[str] = None
    created_at: typing.Optional[int] = None
    tokens: typing.Optional[int] = None
    indexing_status: typing.Optional[str] = None
    error: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    disabled_at: typing.Optional[int] = None
    disabled_by: typing.Optional[str] = None
    archived: typing.Optional[bool] = None
    display_status: typing.Optional[str] = None
    word_count: typing.Optional[int] = None
    hit_count: typing.Optional[int] = None
    doc_form: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
