from datetime import datetime
from typing import Literal, TypedDict

from pytz.tzinfo import BaseTzInfo


class ChurchSuiteCategoryDict(TypedDict):
    """https://github.com/ChurchSuite/churchsuite-api/blob/master/modules/embed.md"""

    id: int
    name: str
    color: str


class ChurchSuiteImageDict(TypedDict):
    """https://github.com/ChurchSuite/churchsuite-api/blob/master/patterns/images.md"""

    px: int
    square: bool
    transparent: bool
    mtime: int
    url: str


class ChurchSuiteImagesDict(TypedDict):
    """https://github.com/ChurchSuite/churchsuite-api/blob/master/patterns/images.md"""

    thumb: ChurchSuiteImageDict
    sm: ChurchSuiteImageDict
    md: ChurchSuiteImageDict
    lg: ChurchSuiteImageDict
    original_16: str
    original_100: str
    original_500: str
    original_1000: str
    square_16: str
    square_100: str


class ChurchSuiteEventDict(TypedDict, total=False):
    """https://github.com/ChurchSuite/churchsuite-api/blob/master/modules/embed.md"""

    id: str
    datetime_start: str
    name: str
    category: ChurchSuiteCategoryDict
    status: Literal["confirmed", "pending", "cancelled"]
    images: ChurchSuiteImagesDict


class Event:
    def __init__(self, object: ChurchSuiteEventDict, timezone: BaseTzInfo) -> None:
        self.object = object
        self.timezone = timezone

    @property
    def id(self) -> str:
        return self.object["id"]

    @property
    def datetime_start(self) -> str:
        return self.object["datetime_start"]

    @property
    def naive_datetime_start(self) -> datetime:
        return datetime.strptime(self.datetime_start, "%Y-%m-%d %H:%M:%S")

    @property
    def localised_datetime_start(self) -> datetime:
        return self.timezone.localize(self.naive_datetime_start)
