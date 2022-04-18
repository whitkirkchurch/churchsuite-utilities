# ChurchSuite Utilities
A Python package for retrieving data from the [ChurchSuite API](https://github.com/ChurchSuite/churchsuite-api).

[![Tests](https://github.com/whitkirkchurch/churchsuite-utilities/actions/workflows/test.yml/badge.svg)](https://github.com/whitkirkchurch/churchsuite-utilities/actions/workflows/test.yml) [![codecov](https://codecov.io/gh/whitkirkchurch/churchsuite-utilities/branch/main/graph/badge.svg?token=xoXJmZoxD8)](https://codecov.io/gh/whitkirkchurch/churchsuite-utilities) [![Total alerts](https://img.shields.io/lgtm/alerts/g/whitkirkchurch/churchsuite-utilities.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/whitkirkchurch/churchsuite-utilities/alerts/) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/whitkirkchurch/churchsuite-utilities.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/whitkirkchurch/churchsuite-utilities/context:python)

## Basic usage

### Retrieving data

To begin with, you'll need to create a new `Account` object.

``` python
import churchsuite

cs = churchsuite.Account(CHURCHSUITE_ACCOUNT)
```
