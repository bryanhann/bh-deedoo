#!/usr/bin/env bash


def stoppersGen():
    def hash4hhmm(hhmm):
        import hashlib
        a=hashlib.md5()
        a.update(hhmm.encode())
        return a.hexdigest()[:4]
    for hh in range(0,24):
        for mm in range(0,60,15):
            hhmm = f"{hh:02}{mm:02}"
            yield hhmm, hash4hhmm(hhmm)



FOR=dict( stoppersGen() )
REV=dict( (v,k) for (k,v) in stoppersGen() )


