#!/usr/bin/env bash
from testing import now

import os
from pathlib import Path
from constants import TEMP
import datetime as DT
import stopping as SH
from testing import now
from stopping import hm4stop, stat4stop
import stopping as SS
from stopping import dt4stop
from stopping import delta4stop
def __dt4stop(stop):
    n = now()
    return DT.datetime( n.year, n.month, n.day, *hm4stop(stop) )

def i__delta4stop(stop):
    return int(now().timestamp() - dt4stop(stop).timestamp())

class BoundsError(Exception): 
    pass


def _answer(stop:str, force=False):
    delta = delta4stop(str(stop))
    if not force and not (0 <= delta < 5*60):
        raise BoundsError
    SS.create4stop(stop)

def answer(stop, force):
    note = input_note()
    print(note)

def __floor15(n): 
    return n-(n%15)
def __truncated_now():
    # change min to 0,15,30,45
    tpl = list(now().timetuple())[:6]
    tpl[4] = floor15(tpl[4])
    return DT.datetime( *tuple(tpl) )
    
