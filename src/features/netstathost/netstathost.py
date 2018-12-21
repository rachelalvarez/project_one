import os

def netstat():
    connections = os.popen('netstat -a').read()
    print("\n connections", connections)