from .util import say, alive, output

from stop import stop4fnow
from stop import delta4stop
from time import sleep
from files import stat4stop, clear
from timing import now

def hhmm4dt(dt):
    return f"{dt.hour}{dt.minute}"
    
def serve () :
    """Start a deedoo server processes.

    It will periodically announce the time,
    and whether a deedoo is outstanding.
    """
    if alive():
        say( "starting deedoo server" )
    clear()
    while alive():
        sleep(0.5)
        stop     = stop4fnow()
        delta    = delta4stop(stop)
        pending  = not stat4stop(stop)
        hhmmss = now().strftime('%H:%M:%S')
        if pending: text = f"{hhmmss} {stop} pending"
        else:       text = f"{hhmmss} {stop} answered" 
        output(text)
        if delta % 300 == 0:
            say( hhmm4dt( now() ) )
            if pending: say( 'deedoo' )
        #if pending and delta % 60 == 0:
        #    say( f"{int(delta/60)} minutes past deedoo" )
    say( "killed" )
