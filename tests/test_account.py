import json
from pathlib import Path

import requests_mock

import churchsuite


def test_base_url():
    cs = churchsuite.Account("test")

    assert cs.base_url == "https://test.churchsuite.com"


def test_calendar_json_url():
    cs = churchsuite.Account("test")

    assert cs.calendar_json_url == "https://test.churchsuite.com/embed/calendar/json"


@requests_mock.Mocker(kw="mock")
def test_get_public_events_response(**kwargs):
    f = open(Path(__file__).with_name("churchsuite_response.json"))
    data = f.read()

    kwargs["mock"].get("https://test.churchsuite.com/embed/calendar/json", text=data)
    cs = churchsuite.Account("test")

    assert cs.get_public_events_response() == json.loads(data)
