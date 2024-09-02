# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .ingestion_success import IngestionSuccess
from .ingestion_error import IngestionError
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class IngestionResponse(UniversalBaseModel):
    successes: typing.List[IngestionSuccess]
    errors: typing.List[IngestionError]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
