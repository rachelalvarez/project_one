from src.features.mainmenu import *

mainmenu.menu()

while True:
    userinput = input().lower()

    def returnstatement():
        print("")
        print("Would you like to select another command? If not, type 'exit'. To list available commands, type 'commands'")

    if userinput == 'exit':
        break

    if userinput == 'commands':
        mainmenu.availablecommands()

    if userinput == "1": # command: Ping current host
        from src.features.pinghost import *
        pinghost.ping()
        returnstatement()

    if userinput == "2": #command: Run netstat on current host
        from src.features.netstathost import *
        netstathost.netstat()
        returnstatement()

    if userinput == "3": #command: Run ARP on current host
        from src.features.arphost import *
        arphost.arp()
        returnstatement()

    if userinput == "4": #command: Run tracert to specific host
        from src.features.tracerthost import *
        print("What host would you like to perform trace route on?")
        tracertans = input()
        str(tracerthost.tracert(tracertans))
        returnstatement()