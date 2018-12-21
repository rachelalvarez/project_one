import os

def arp():
    arplist = os.popen('arp -a').read()
    print(arplist)

arp()