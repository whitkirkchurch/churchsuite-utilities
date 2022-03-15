import pytz
import requests

CHURCHSUITE_BASE_DOMAIN = "churchsuite.com"

TZ_LONDON = pytz.timezone("Europe/London")


class Account:
    def __init__(self, account_id, timezone=TZ_LONDON):
        self.account_id = account_id
        account_timezone = timezone

    @property
    def base_url(self):
        return "https://{churchsuite_account_id}.{domain}".format(
            churchsuite_account_id=self.account_id, domain=CHURCHSUITE_BASE_DOMAIN
        )

    @property
    def calendar_json_url(self):
        return "{base_url}/embed/calendar/json".format(base_url=self.base_url)

    def get_public_events(self, params={}):
        resp = requests.get(url=self.calendar_json_url, params=params)
        return resp.json()
