# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .update_document_by_file_response_document import (
    UpdateDocumentByFileResponseDocument,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class UpdateDocumentByFileResponse(UniversalBaseModel):
    document: typing.Optional[UpdateDocumentByFileResponseDocument] = None
    batch: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
