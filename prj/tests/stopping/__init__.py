import datetime as DT
from constants import FOR, REV, TEMP
from testing import floor4now as TNOW
from util import zstrip
from testing import now
def __rm4pth(pth): pth.exists() and pth.unlink()
def __path4stop(stop): return TEMP/stop
def create4stop(stop) : __path4stop(stop).touch()
def remove4stop(stop) : __rmpth( __path4stop(stop) )
def stat4stop(stop)   : return __path4stop(stop).exists()

def floor5hhmm(hhmm):
    keys = [ x for x in FOR.keys() ]
    keys.reverse()
    for key in keys:
        if key <= hhmm:
           return key

def hhmm4stop(stop): return REV[stop.lower()]
def hhmm4dt(dt)    : return f"{dt.hour:02}{dt.minute:02}"
def hhmm4now()     : return hhmm4dt( TNOW() )
def clear()        : [x.unlink() for x in TEMP.glob('*')]
def list()         : [ print(x) for x in TEMP.glob('*') ]
def hm4hhmm(hhmm): return eval(zstrip(hhmm[:2])), eval(zstrip(hhmm[-2:]))



def stop4now()     : return FOR[ hhmm4now() ]
def hm4stop(stop)  : return hm4hhmm( hhmm4stop( stop ))
def dt4stop(stop):
    n = now()
    return DT.datetime( n.year, n.month, n.day, *hm4stop(stop) )

def delta4stop(stop):
    return int(now().timestamp() - dt4stop(stop).timestamp())

