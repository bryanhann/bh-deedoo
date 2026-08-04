from fn       import hhmm4stop
from .hm4hhmm import hm4hhmm

def hm4stop(stop):
    return hm4hhmm( hhmm4stop( stop ))

def test_0000(): assert hm4stop('4a7d') == (0,0)
def test_1645(): assert hm4stop('C1FE') == (16,45)
