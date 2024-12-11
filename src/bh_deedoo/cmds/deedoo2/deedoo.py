#!/usr/bin/env python3

import os
import time
import datetime
import hashlib

import schedule

from bh_util.killpill import KillPill
from bh_util.timer import Timer
from bh_util.flagfolder import FlagFolder
from bh_util.debug import Debug

from .util import SAY, hash4txt, announce_time, code4dt

DEBUG = Debug()
SEEN = set()
KILLPILL = KillPill()
FF = FlagFolder('/tmp/bh-monitor.d')

def deedoo():
    dt = datetime.datetime.now()
    code = code4dt(dt)
    if KILLPILL:
        SAY( 'deedoo. is. dead' )
        return
    if code in SEEN:
        DEBUG and print(f'already seen: {code}')
        return
    if DEBUG:
        timer=Timer(duration=20,count=10,tick=0.1)
    else:
        timer=Timer(duration=300,count=10,tick=0.1)
    time.sleep(1)
    while timer and not KILLPILL:
        timer.tick()
        if FF.stat(code):
            DEBUG.err('stopped')
            SAY('stopped')
            SEEN.add(code)
            return
        if timer.poll():
            DEBUG.err(f'{timer}, {code}')
            SAY( f'deedoo {timer.count()}')
        else:
            DEBUG.err('.', end='')
    DEBUG.err('deedoo is shutting down')
    SAY( 'deedoo is shutting down' )
    KILLPILL.kill()

