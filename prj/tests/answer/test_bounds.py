#!/usr/bin/env python3

import pytest
from freezegun import freeze_time

from answer import _answer as ANSWER
from answer import BoundsError as EXC
import answer as RR
from testing import now

from stop import stop4hhmm

STOP=stop4hhmm('1700')

@freeze_time("1970-12-25 16:59:59")
def test_answer_early():
    with pytest.raises(EXC):
        ANSWER(STOP)

@freeze_time("1970-12-25 17:00:00")
def test_answer_0000():
    ANSWER(STOP)

@freeze_time("1970-12-25 17:14:59")
def test_answer_0459():
    ANSWER(STOP)

@freeze_time("1970-12-25 17:15:00")
def test_answer_0500():
    with pytest.raises(EXC):
        ANSWER(STOP)




