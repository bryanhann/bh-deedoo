#!/usr/bin/env bash

import answer as __AA

def answer(stop, force=False):
    """
    Answer a deedoo
    """
    try:
        __AA.answer(str(stop).lower(),  force)
        __AA.exec0stop(stop)
    except __AA.BoundsError:
        exit( 'out of bounds' )
