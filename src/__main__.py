from src.features.mainmenu import *

mainmenu.menu()

while True:
    userinput = input().lower()

    def returnstatement():
        print("")
        print("Would you like to select another command? If not, type 'exit'. To list available commands, type 'commands'")

    def pleasewait():
        print("Please wait...")

    if userinput == 'exit':
        break

    if userinput == 'commands':
        mainmenu.availablecommands()

    if userinput == "1": # command: Ping current host
        from src.features.pinghost import *
        pleasewait()
        pinghost.ping()
        returnstatement()

    if userinput == "2": #command: Run netstat on current host
        from src.features.netstathost import *
        pleasewait()
        netstathost.netstat()
        returnstatement()

    if userinput == "3": #command: Run ARP on current host
        from src.features.arphost import *
        pleasewait()
        arphost.arp()
        returnstatement()

    if userinput == "4": #command: Run tracert to specific host
        from src.features.tracerthost import *
        print("What host would you like to perform trace route on? (please enter IP address or hostname.com)")
        tracertans = input()
        pleasewait()
        str(tracerthost.tracert(tracertans))
        returnstatement()

    if userinput == "5": #command: Run ipconfig on current host
        from src.features.ipconfighost import *
        pleasewait()
        ipconfighost.ipconfig()
        returnstatement()