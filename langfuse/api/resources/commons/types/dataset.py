# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Dataset(UniversalBaseModel):
    id: str
    name: str
    description: typing.Optional[str] = None
    metadata: typing.Optional[typing.Optional[typing.Any]] = None
    project_id: str = pydantic.Field(alias="projectId")
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
