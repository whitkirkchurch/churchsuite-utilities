import pytz
import requests

from . import events

CHURCHSUITE_BASE_DOMAIN = "churchsuite.com"

TZ_LONDON = pytz.timezone("Europe/London")


class Account:
    def __init__(self, account_id, timezone=TZ_LONDON):
        self.account_id = account_id
        self.account_timezone = timezone

    @property
    def base_url(self):
        return f"https://{self.account_id}.{CHURCHSUITE_BASE_DOMAIN}"

    @property
    def calendar_json_url(self):
        return f"{self.base_url}/embed/calendar/json"

    def get_public_events_response(self, params=None):
        if not params:
            params = {}
        response = requests.get(url=self.calendar_json_url, params=params)
        return response.json()

    def get_public_events(self, params=None):
        response = self.get_public_events_response(params)
        return map(lambda e: events.Event(e, self.account_timezone), response)
