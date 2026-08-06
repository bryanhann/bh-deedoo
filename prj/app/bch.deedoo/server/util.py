import sys
import os
from pathlib import Path

BACKSPACES = '\b'*100
BLANKS = ' ' * 60
CLEAR = BACKSPACES + BLANKS + BACKSPACES

def say(text):
    os.system(f"say {text}")

def alive():
     return not (Path.home()/'die').exists()

def output( text ):
    sys.stdout.write( f"{CLEAR}{text}" )
    sys.stdout.flush()
