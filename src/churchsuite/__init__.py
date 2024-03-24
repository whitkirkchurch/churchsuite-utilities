from typing import Any, Optional, TypedDict

import pytz
import requests
from pytz.tzinfo import BaseTzInfo

from . import events
from .events import Event

CHURCHSUITE_BASE_DOMAIN = "churchsuite.com"

TZ_LONDON: BaseTzInfo = pytz.timezone("Europe/London")

ChurchSuiteEventsParametersDict = dict[str, Any]


class ChurchSuiteEventDict(TypedDict, total=False):
    id: str
    datetime_start: str


class Account:
    def __init__(self, account_id: str, timezone: BaseTzInfo = TZ_LONDON) -> None:
        self.account_id = account_id
        self.account_timezone = timezone

    @property
    def base_url(self) -> str:
        return f"https://{self.account_id}.{CHURCHSUITE_BASE_DOMAIN}"

    @property
    def calendar_json_url(self) -> str:
        return f"{self.base_url}/embed/calendar/json"

    def get_public_events_response(
        self, params: Optional[ChurchSuiteEventsParametersDict] = None
    ) -> list[ChurchSuiteEventDict]:
        if not params:
            params = {}
        response = requests.get(url=self.calendar_json_url, params=params)
        parsed_response: list[ChurchSuiteEventDict] = response.json()
        return parsed_response

    def get_public_events(
        self, params: Optional[ChurchSuiteEventsParametersDict] = None
    ) -> list[Event]:
        response = self.get_public_events_response(params)
        return [events.Event(e, self.account_timezone) for e in response]
