#from constants import TEMP

from .temp import TEMP

def _rm4pth(pth): 
    pth.exists() and pth.unlink()

def create4stop(stop) : 
    path4stop(stop).touch()

def remove4stop(stop) : 
    _rmpth( path4stop(stop) )

def path4stop(stop): 
    """Diagmostic: return cached stop
    """
    return TEMP/stop

def stat4stop(stop):
    """Is stop in the cache?
    """
    return path4stop(stop).exists()


def clear(): 
    """Clear all stored stops.

    Typically called before starting a server.
    """
    [x.unlink() for x in TEMP.glob('*')]

def list():
    """list all stored stop
    """
