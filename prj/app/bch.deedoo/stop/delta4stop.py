from .dt4now  import dt4now
from .dt4stop import dt4stop

def delta4stop(stop):
    t1 = dt4now().timestamp()
    t0 = dt4stop(stop).timestamp()
    return int(t1-t0)

#######################################

from freezegun import freeze_time
from .stop4hhmm import stop4hhmm

STOP=stop4hhmm('1700')

@freeze_time("1970-12-25 17:01:02")
def test_delta():
    assert delta4stop(STOP) == 62

@freeze_time("1970-12-25 16:59:59")
def test_delta_early():
    assert delta4stop(STOP) == -1

