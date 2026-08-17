#!/usr/bin/env python3

def now():
    import datetime as DT
    return DT.datetime.now()
 
def floor4now():
    import datetime as DT
    def floor15(n): return n-(n%15)
    # change min to 0,15,30,45
    tpl = list(now().timetuple())[:6]
    tpl[4] = floor15(tpl[4])
    return DT.datetime( *tuple(tpl) )
    
