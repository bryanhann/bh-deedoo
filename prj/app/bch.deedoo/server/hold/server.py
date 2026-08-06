from stop import stop4fnow
from stop import delta4stop
from time import sleep
from files import stat4stop, clear
import sys
import os
from timing import now
from pathlib import Path
BACKSPACES = '\b'*100
BLANKS = ' ' * 60
CLEAR = BACKSPACES + BLANKS + BACKSPACES
def say(text):
    os.system(f"say {text}")

while True and 0:
    dt=now()
    print( dt.strftime('%H:%M:%S') )
    sleep(1)
def alive():
     return not (Path.home()/'die').exists()

def output( text ):
    sys.stdout.write( f"{CLEAR}{text}" )
    sys.stdout.flush()
def serve () :
    say( "starting deedoo" )
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
        if pending and delta % 60 == 0:
            say( f"{int(delta/60)} minutes past deedoo" )

