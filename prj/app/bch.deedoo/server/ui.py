from stop import stop4fnow
from stop import delta4stop
from time import sleep
from files import stat4stop, clear
import sys
import os
from timing import now
from pathlib import Path
def say(text):
    os.system(f"say {text}")

def alive():
     return not (Path.home()/'die').exists()


def pending():
    sleep(0.1)
    stop=stop4fnow()
    return stat4stop(stop) and stop or ''
def mind () :
    say( "starting minder" )
    clear()
    while alive():
        sleep(0.5)
        stop=stop4fnow()
        stopped=stat4stop(stop)
        if stopped:
            print('.')
        else:
            delta = delta4stop(stop)
            print(stop, delta)
            if delta % 60 == 0:
               say( f"{int(delta/60)} minutes past deedoo" )

