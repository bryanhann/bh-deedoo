#!/usr/bin/env bash
import datetime as DT
import constants as CC

def now(): return DT.datetime.now()
def hhmm4stop(stop:str): return CC.REV[stop.lower()]
def hm4stop(stop): return hm4hhmm( hhmm4stop( stop ))
def clear(): [x.unlink() for x in CC.TEMP.glob('*')]
def list(): [ print(x) for x in CC.TEMP.glob('*') ]

def hm4hhmm(hhmm):
    def zstrip( x : str ):
        while x.startswith('0'):
            x=x[1:] 
        return x and x or '0'
    h = eval(zstrip(hhmm[:2]))
    m = eval(zstrip(hhmm[-2:]))
    return (h,m)


def stat4stop(stop):
    return path4stop(stop).exists()
def input_note():
    acc = []
    while not acc[-2:] == ['','']:
        acc.append( input('> ') )
    return '\n'.join(acc[:-2])

def path4stop(stop): 
    return CC.TEMP/stop
