#!/usr/bin/env python3

from stopping import hm4stop as FN

def test_0000(): assert FN('4a7d') == (0,0)
def test_1645(): assert FN('C1FE') == (16,45)

