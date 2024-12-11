#!/usr/bin/env python3

import os
import datetime
import hashlib

def SAY(text):
    os.system(f'say {text}')

def hash4txt(text):
    a=hashlib.md5()
    a.update(text.encode())
    return a.hexdigest()[:4]


def announce_time():
    dt=datetime.datetime.now()
    hh = dt.strftime("%H")
    mm = dt.strftime("%M")
    if mm == '00': text = f"{hh} hundred"
    else:          text = f"{hh} {mm}"
    SAY(f"The time is {text}")

def code4dt(dt):
    def hhmm4dt(dt):
        return dt.strftime("%H%M")
    return hash4txt(hhmm4dt(dt))

