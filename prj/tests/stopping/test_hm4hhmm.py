#!/usr/bin/env python3

from stopping import hm4hhmm as FN

def test_2345(): assert FN('2345')==(23, 45)
def test_0305(): assert FN('0305')==(3,5)
def test_0000(): assert FN('0000')==(0,0)

