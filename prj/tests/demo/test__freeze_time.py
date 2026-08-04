#!/usr/bin/env python3

from freezegun import freeze_time

def now () :
    import datetime
    return datetime.datetime.now()

@freeze_time("1970-12-25 17:01:02")
def test_marker_freeze_time_decorator():
    n = now()
    assert now().year == 1970
    
def test_marker_freeze_time_context_manager():
    with freeze_time("1971-12-25 17:01:02"):
        assert now().year == 1971

