import socket, subprocess, os


def ping():
    try:
        userip = socket.gethostbyname(socket.gethostname()) #returns the local host's IP address
        results = subprocess.check_output(["ping", "-c", "1", userip])
        print("Host Results: " + str(results))
        print("")
        print("Host is UP & HEALTHY")
    except subprocess.CalledProcessError as e:
        print("Host is DOWN & UNHEALTHY")