#!/usr/bin/env python3

def zstrip( x : str ):
    while x.startswith('0'):
        x=x[1:] 
    return x and x or '0'

