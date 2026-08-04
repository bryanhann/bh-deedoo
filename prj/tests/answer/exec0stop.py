#!/usr/bin/env bash

import os

def exec0stop(stop):
    print( f"touched {stop}" )    
    os.system('say touched')
    cmd=f"bh deedoo answer {stop}"
    os.system( cmd )

