#!/usr/bin/env bash

from pathlib import Path

def stoppersGen():
    def hash4hhmm(hhmm):
        import hashlib
        a=hashlib.md5()
        a.update(hhmm.encode())
        return a.hexdigest()[:4]
    for hh in range(0,24):
        for mm in range(0,60,15):
            hhmm = f"{hh:02}{mm:02}"
            yield hhmm, hash4hhmm(hhmm)


TEMP=Path.home()/'.tmp'
TEMP.is_dir() or TEMP.mkdir()
TEMP=TEMP/'deedoo2315'
TEMP.is_dir() or TEMP.mkdir()

FOR=dict( stoppersGen() )
REV=dict( (v,k) for (k,v) in stoppersGen() )

STOP = '01e0'

