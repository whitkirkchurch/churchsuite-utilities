# ChurchSuite Utilities
A Python package for retrieving data from the [ChurchSuite API](https://github.com/ChurchSuite/churchsuite-api).

[![Tests](https://github.com/whitkirkchurch/churchsuite-utilities/actions/workflows/test.yml/badge.svg)](https://github.com/whitkirkchurch/churchsuite-utilities/actions/workflows/test.yml) [![codecov](https://codecov.io/gh/whitkirkchurch/churchsuite-utilities/branch/main/graph/badge.svg?token=xoXJmZoxD8)](https://codecov.io/gh/whitkirkchurch/churchsuite-utilities)

## Basic usage

### Instantiating an `Account` object

To begin with, you'll need to create a new `Account` object. It requires one argument, the ChurchSuite account ID (that's the bit before "churchsuite.com" in the URL):

``` python
import churchsuite

CHURCHSUITE_ACCOUNT = "whitkirk"

cs = churchsuite.Account(CHURCHSUITE_ACCOUNT)
```

Optionally, you can pass an instance of a [pytz](http://pytz.sourceforge.net/) `timezone` as the second argument to use in date/time localisation. This defaults to `Europe/London`, since this is where most ChurchSuite sites are located.

``` python
import churchsuite
import pytz

CHURCHSUITE_ACCOUNT = "whitkirk"

cs = churchsuite.Account(CHURCHSUITE_ACCOUNT, pytz.timezone("Europe/London"))
```

Once you've got an instance of `Account` you can use it to make calls to ChurchSuite.

### Getting public events

You can pull events from a public ChurchSuite calendar using `get_public_events()`:

``` python
events = cs.get_public_events()
```

In the background this makes a call to the [ChurchSuite calendar JSON feed](https://github.com/ChurchSuite/churchsuite-api/blob/master/modules/embed.md#calendar-json-feed).

You can also pass in a dictionary of parameters to use in this query (see the [ChurchSuite API docs](https://github.com/ChurchSuite/churchsuite-api/blob/master/modules/embed.md#calendar-json-feed) for a full list), for example to only return featured event:

``` python
events = cs.get_public_events({
  featured: 1
})
```

`get_public_events()` returns a list of `Event`s which match the query.

#### The `Event` object

Each `Event` object has a few helper methods to retrieve useful things from the ChurchSuite event.

If you want to access the contents of the returned object directly, you can use the `Event.object` property:

``` python
for event in events:
  print(event.object['id'])
```

##### Date/time helpers

ChurchSuite's JSON returns dates and times as strings. There's a helper method to turn these directly into Python `datetime` objects:

``` python
for event in events:
  print(event.naive_datetime_start)
```

These objects are naive, without any timezone information (ie they are always in the _local_ time of the event, which can cause problems when straddling daylight saving boundaries). You can interpret them through the lens of the timezone provided to the `Account` object using `localised_datetime_start`.

``` python
for event in events:
  print(event.localised_datetime_start)
```
