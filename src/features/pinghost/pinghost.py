import socket, subprocess


def pinghost():
    userip = socket.gethostbyname(socket.gethostname()) #returns the local host's IP address
    results = subprocess.check_output(["ping", "-c", "1", userip])
    print(results)