#!/usr/bin/env bash
import os
import stopping as SS

class BoundsError(Exception): 
    pass

def _answer(stop:str, force=False):
    delta = SS.delta4stop(str(stop))
    if not force and not (0 <= delta < 30*60):
        raise BoundsError
    SS.create4stop(stop)

def answer(stop, force=False):
    stop=str(stop).lower()
    _answer(stop, force)
    #note = input_note()
    #print(note)
    cmd=f"bh deedoo answer {stop}"
    print(cmd)
    os.system( cmd )

    
