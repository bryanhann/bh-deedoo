#!/usr/bin/env python3
from freezegun import freeze_time

from testing import floor4now as TNOW


def hhmm4dt(dt):
    return f"{dt.hour:02}{dt.minute:02}"

@freeze_time("1970-12-25 17:00:00")
def test_1700(): 
    assert hhmm4dt( TNOW() ) =='1700'

@freeze_time("1970-12-25 17:14:00")
def test_1714():
    assert hhmm4dt( TNOW() ) =='1700'

@freeze_time("1970-12-25 17:15:00")
def test_1715():
    assert hhmm4dt( TNOW() ) =='1715'

@freeze_time("1970-12-25 17:29:00")
def test_1729(): 
    assert hhmm4dt( TNOW() ) =='1715'



@freeze_time("1970-12-25 17:30:00")
def test_1730():
    assert hhmm4dt( TNOW() ) =='1730'

@freeze_time("1970-12-25 17:44:00")
def test_1744():
    assert hhmm4dt( TNOW() ) =='1730'


@freeze_time("1970-12-25 17:45:01")
def test_1759():
    assert hhmm4dt( TNOW() ) =='1745'

@freeze_time("1970-12-25 17:59:00")
def test_1759(): 
    assert hhmm4dt( TNOW() ) =='1745'

