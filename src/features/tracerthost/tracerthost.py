import os, sys

def tracert(userinput):
    syscheck = sys.platform
    if syscheck is 'linux' or 'darwin':
        tracertresults = os.popen('traceroute ' + userinput).read()
        print(tracertresults)
        print("TRACE ROUTE COMPLETE")
    elif syscheck is 'win32' or 'cygwin':
        tracertresults = os.popen('tracert ' + userinput).read()
        print(tracertresults)
        print("TRACE ROUTE COMPLETE")