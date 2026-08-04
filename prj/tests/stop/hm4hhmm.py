from util import zstrip

def hm4hhmm(hhmm): 
    """Convert hhmm to a pair of ints
    """
    return eval(zstrip(hhmm[:2])), eval(zstrip(hhmm[-2:]))
def test_2345(): assert hm4hhmm('2345')==(23, 45)
def test_0305(): assert hm4hhmm('0305')==(3,5)
def test_0000(): assert hm4hhmm('0000')==(0,0)

