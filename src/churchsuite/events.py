from datetime import datetime


class Event:
    def __init__(self, object, timezone):
        self.object = object
        self.timezone = timezone

    def get_field(self, field):
        return self.object[field]

    @property
    def id(self):
        return self.get_field("id")

    @property
    def datetime_start(self):
        return self.get_field("datetime_start")

    @property
    def naive_datetime_start(self):
        return datetime.strptime(self.datetime_start, "%Y-%m-%d %H:%M:%S")

    @property
    def localised_datetime_start(self):
        return self.timezone.localize(self.naive_datetime_start)
