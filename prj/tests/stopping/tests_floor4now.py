#!/usr/bin/env python3

from freezegun import freeze_time
from constants import FOR
from stopping import floor5hhmm, stop4now, hhmm4dt, hhmm4now
from testing import floor4now as TNOW

def _assert(hhmm):
    assert hhmm4now() == hhmm
    assert FOR[hhmm] == stop4now()

def test_floor_1700(): assert floor5hhmm('1714') == '1700'
def test_floor_1714(): assert floor5hhmm('1714') == '1700'
def test_floor_1715(): assert floor5hhmm('1715') == '1715'
def test_floor_1759(): assert floor5hhmm('1759') == '1745'


@freeze_time("1970-12-25 17:00:00")
def test_1700(): _assert( '1700' )

@freeze_time("1970-12-25 17:14:00")
def test_1714(): _assert( '1700' )

@freeze_time("1970-12-25 17:15:00")
def test_1715(): _assert( '1715' )

@freeze_time("1970-12-25 17:29:00")
def test_1729(): _assert( '1715' )

@freeze_time("1970-12-25 17:30:00")
def test_1730(): _assert( '1730' )

@freeze_time("1970-12-25 17:44:00")
def test_1744(): _assert( '1730' )

@freeze_time("1970-12-25 17:45:01")
def test_1759(): _assert( '1745' )

@freeze_time("1970-12-25 17:59:00")
def test_1759(): _assert( '1745' )

