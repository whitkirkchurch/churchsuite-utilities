import churchsuite


def test_base_url():
    cs = churchsuite.Account("test")

    assert cs.base_url == "https://test.churchsuite.com"


def test_calendar_json_url():
    cs = churchsuite.Account("test")

    assert cs.calendar_json_url == "https://test.churchsuite.com/embed/calendar/json"
