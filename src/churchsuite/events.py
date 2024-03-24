from datetime import datetime

from pytz.tzinfo import BaseTzInfo

from . import ChurchSuiteEventDict


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
