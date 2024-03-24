import json
from pathlib import Path

import churchsuite
import requests_mock


def test_base_url():
    cs = churchsuite.Account("test")

    assert cs.base_url == "https://test.churchsuite.com"


def test_calendar_json_url():
    cs = churchsuite.Account("test")

    assert cs.calendar_json_url == "https://test.churchsuite.com/embed/calendar/json"


@requests_mock.Mocker(kw="mock")
def test_get_public_events_response(**kwargs):
    with open(Path(__file__).with_name("churchsuite_response.json")) as f:
        data = f.read()

        kwargs["mock"].get(
            "https://test.churchsuite.com/embed/calendar/json", text=data
        )
        cs = churchsuite.Account("test")

        assert cs.get_public_events_response() == json.loads(data)
