#!/usr/bin/env python3

import pytest
from freezegun import freeze_time

from constants import STOP
from answering import _answer as ANSWER
from answering import BoundsError as EXC
import answering as RR
from testing import now


@freeze_time("1970-12-25 16:59:59")
def test_answer_early():
    with pytest.raises(EXC):
        ANSWER(STOP)
@freeze_time("1970-12-25 17:00:00")
def test_answer_0000():
    ANSWER(STOP)

@freeze_time("1970-12-25 17:01:02")
def test_answer_0102():
    ANSWER(STOP)

@freeze_time("1970-12-25 17:04:49")
def test_answer_0459():
    ANSWER(STOP)

@freeze_time("1970-12-25 17:05:00")
def test_answer_0500():
    with pytest.raises(EXC):
        ANSWER(STOP)




