#from constants import REV
from stop.misc import REV
def hhmm4stop(stop):
    return REV[stop.lower()]


def test_lowercase():  assert hhmm4stop('46a5')=='2300'
def test_uppercase():  assert hhmm4stop('46A5')=='2300'


