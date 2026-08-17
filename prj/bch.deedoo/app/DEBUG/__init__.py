#!/usr/bin/env python3

"""DEBUG MODE

If the file [~/DEBUG] exists in the user's home 
directory, import extra stuff.
"""
import pathlib
if (pathlib.Path.home()/'DEBUG').exists():
    from DEBUG.stuff import *
    DEBUG=True
else:
    DEBUG=False
del pathlib
