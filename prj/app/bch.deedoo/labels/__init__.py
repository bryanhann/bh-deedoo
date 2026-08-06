#!/usr/bin/env python3
#exit()
from stop import FOR    

def label(*args):
    """Print labels to stdout, suitable for printing.

    ARGS is list of deedoo times (eg, 1715).
    """
    keys = [ f"{x:04}" for x in args ]
    vals = [ FOR[x] for x in keys ]
    keys = ' '.join(keys)
    vals = ' '.join(vals)
    print(keys)
    print(vals)

