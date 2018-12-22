import os, sys

def ipconfig():
    syscheck = sys.platform
    if syscheck is 'linux' or 'darwin':
        ipconfigresults = os.popen('ifconfig').read()
        print(ipconfigresults)
        print("IPCONFIG COMPLETE")
    elif syscheck is 'win32' or 'cygwin':
        ipconfigresults = os.popen('ipconfig').read()
        print(ipconfigresults)
        print("IPCONFIG COMPLETE")