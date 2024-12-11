#!/usr/bin/env python3
import time

import typer
import schedule

from bh_util.killpill import KillPill
from bh_util.flagfolder import FlagFolder
from bh_util.debug import Debug

from .util import announce_time
from .deedoo import deedoo

DEBUG = Debug()
KILLPILL = KillPill()

FF = FlagFolder('/tmp/bh-monitor.d')

app = typer.Typer()

@app.command()
def test():
    deedoo()

@app.command()
def answer(code : str ):
    FF.set(code)

@app.command()
def run(debug : bool = False):
    if debug:
        schedule.every(10).seconds.do(deedoo)
        DEBUG.turn_on()
    else:
        schedule.every(5).minutes.do(announce_time)
        schedule.every(15).minutes.do(deedoo)
        DEBUG.turn_off()
    KILLPILL.clear()
    FF.clear_all()
    announce_time()
    while True:
        schedule.run_pending()
        time.sleep(1)

