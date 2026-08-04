#!/usr/bin/env python3

from freezegun import freeze_time

from constants import STOP
from reverse import _answer
from answering import clear, list, stat4stop

@freeze_time("1970-12-25 17:04:49")
def test_path4stop():
    clear()
    assert not stat4stop(STOP)
    _answer(STOP)
    list()
    assert stat4stop(STOP)
    clear()
    assert not stat4stop(STOP)

