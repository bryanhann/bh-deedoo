from .misc import FOR
from .         import hhmm4fnow
def stop4fnow(): 
    return FOR[ hhmm4fnow() ]

##############################################3
from freezegun import freeze_time

def _assert(hhmm):
    assert FOR[hhmm] == stop4fnow()



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

