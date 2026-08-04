#!/usr/bin/env python3

from freezegun import freeze_time

from constants import STOP
from stopping import delta4stop as FN

@freeze_time("1970-12-25 17:01:02")
def test_delta():
    assert FN(STOP) == 62

@freeze_time("1970-12-25 16:59:59")
def test_delta_early():
    assert FN(STOP) == -1

