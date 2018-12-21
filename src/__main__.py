from src.features.mainmenu import *

mainmenu.menu()

while True:
    userinput = input().lower()

    def returnstatement():
        print("")
        print("Would you like to select another? If not, type 'exit'. To list available commands, type 'commands'")

    if userinput == 'exit':
        break

    if userinput == 'commands':
        mainmenu.availablecommands()

    if userinput == "1": # command: Ping current host
        from src.features.pinghost import *
        pinghost.ping()
        returnstatement()