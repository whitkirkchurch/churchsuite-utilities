import json
from datetime import datetime
from pathlib import Path

import pytz

from churchsuite import events


def event_factory():
    with open(Path(__file__).with_name("churchsuite_response.json")) as f:
        data = json.load(f)
        return events.Event(data[0], pytz.timezone("Europe/London"))


def test_id():
    event = event_factory()

    assert event.id == 1127446


def test_datetime_start():
    event = event_factory()

    assert event.datetime_start == "2022-02-14 00:00:00"


def test_naive_datetime_start():
    event = event_factory()

    assert event.naive_datetime_start == datetime(2022, 2, 14, 0, 0)


def test_localised_datetime_start_has_timezone():
    event = event_factory()

    assert event.localised_datetime_start.tzinfo is not None


def test_localised_datetime_start_is_correct():
    event = event_factory()

    assert event.localised_datetime_start.replace(tzinfo=None) == datetime(
        2022, 2, 14, 0, 0
    )
