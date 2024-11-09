import json
from datetime import datetime
from pathlib import Path

import pytz

from churchsuite import events


def events_factory():
    with open(Path(__file__).with_name("churchsuite_response.json")) as f:
        data = json.load(f)
        return [events.Event(e, pytz.timezone("Europe/London")) for e in data]


def test_id():
    event = events_factory()[0]

    assert event.id == 1127446


def test_datetime_start():
    event = events_factory()[0]

    assert event.datetime_start == "2022-08-14 18:00:00"


def test_naive_datetime_start_is_correct_in_bst():
    event = events_factory()[0]

    assert event.naive_datetime_start == datetime(2022, 8, 14, 18, 0)


def test_naive_datetime_start_is_correct_in_gmt():
    event = events_factory()[1]

    assert event.naive_datetime_start == datetime(2022, 2, 14, 18, 0)


def test_naive_datetime_start_has_no_timezone_in_bst():
    event = events_factory()[0]

    assert event.naive_datetime_start.tzinfo is None


def test_naive_datetime_start_has_no_timezone_in_gmt():
    event = events_factory()[1]

    assert event.naive_datetime_start.tzinfo is None


def test_localised_datetime_start_has_timezone_in_bst():
    event = events_factory()[0]

    assert event.localised_datetime_start.tzinfo is not None


def test_localised_datetime_start_has_timezone_in_gmt():
    event = events_factory()[1]

    assert event.localised_datetime_start.tzinfo is not None


def test_localised_datetime_start_is_correct_in_bst():
    event = events_factory()[0]

    assert event.localised_datetime_start.replace(tzinfo=None) == datetime(
        2022, 8, 14, 18, 00
    )


def test_localised_datetime_start_is_correct_in_gmt():
    event = events_factory()[1]

    assert event.localised_datetime_start.replace(tzinfo=None) == datetime(
        2022, 2, 14, 18, 00
    )


def test_localised_datetime_renders_correctly_in_bst():
    event = events_factory()[0]

    assert (
        event.localised_datetime_start.strftime("%Y-%m-%d %H:%M:%S")
        == "2022-08-14 18:00:00"
    )


def test_localised_datetime_renders_correctly_in_gmt():
    event = events_factory()[1]

    assert (
        event.localised_datetime_start.strftime("%Y-%m-%d %H:%M:%S")
        == "2022-02-14 18:00:00"
    )
