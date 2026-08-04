#!/usr/bin/env python3

import stopping as SS

FN=SS.hhmm4stop

def test_lowercase():  assert FN('46a5')=='2300'
def test_uppercase():  assert FN('46A5')=='2300'


