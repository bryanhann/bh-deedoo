#!/usr/bin/env python3

from freezegun import freeze_time

from answer    import answer
from files     import clear, list, stat4stop
from stop      import stop4hhmm
STOP=stop4hhmm('1700')

@freeze_time("1970-12-25 17:04:49")
def test_path4stop():
    clear()
    assert not stat4stop(STOP)
    answer(STOP)
    list()
    assert stat4stop(STOP)
    clear()
    assert not stat4stop(STOP)

