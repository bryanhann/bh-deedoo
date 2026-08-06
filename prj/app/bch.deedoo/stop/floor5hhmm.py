#from constants import FOR
from .misc import FOR
def floor5hhmm(hhmm):
    """Reduce hhmm until it matches a deedoo
    """
    hhmm=str(hhmm)
    keys = [ x for x in FOR.keys() ]
    keys.reverse()
    for key in keys:
        if key <= hhmm:
           return key


def test_floor_1700(): assert floor5hhmm('1714') == '1700'
def test_floor_1714(): assert floor5hhmm('1714') == '1700'
def test_floor_1715(): assert floor5hhmm('1715') == '1715'
def test_floor_1759(): assert floor5hhmm('1759') == '1745'


