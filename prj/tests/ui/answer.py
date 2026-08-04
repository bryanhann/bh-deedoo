#!/usr/bin/env bash

import answer.ui as UU

def answer(stop, force=False):
    try:
        UU.answer(str(stop).lower(),  force)
        UU.exec0stop(stop)
    except UU.BoundsError:
        exit( 'out of bounds' )
