# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class BasePrompt(UniversalBaseModel):
    name: str
    version: int
    config: typing.Optional[typing.Any] = None
    labels: typing.List[str] = pydantic.Field()
    """
    List of deployment labels of this prompt version.
    """

    tags: typing.List[str] = pydantic.Field()
    """
    List of tags. Used to filter via UI and API. The same across versions of a prompt.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
