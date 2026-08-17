import datetime
from timing import now as NOW
from fn import hhmm4stop
from .hm4hhmm import hm4hhmm


def dt4stop(stop):
    n = NOW()
    h,m = hm4hhmm(hhmm4stop( stop ))
    return datetime.datetime( n.year, n.month, n.day, h, m )



