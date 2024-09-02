# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from ...commons.types.dataset_run import DatasetRun
from ...utils.resources.pagination.types.meta_response import MetaResponse
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PaginatedDatasetRuns(UniversalBaseModel):
    data: typing.List[DatasetRun]
    meta: MetaResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
