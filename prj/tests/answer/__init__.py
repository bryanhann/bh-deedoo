#!/usr/bin/env bash

class BoundsError(Exception):
    pass

def _answer(stop:str, force=False):
    from stop      import stop4fnow
    from files     import create4stop
    from constants import REV
    if not stop in REV:
        exit( "bad stop" )
    if force or stop == stop4fnow():
        create4stop(stop)
    else:
        raise BoundsError

def exec0stop(stop):
    import os
    print( f"touched {stop}" )    
    os.system('say touched')
    cmd=f"bh deedoo answer {stop}"
    os.system( cmd )

def answer(stop, force=False):
    try:
        _answer(str(stop).lower(),  force)
        exec0stop(stop)
    except BoundsError:
        exit( 'out of bounds' )
