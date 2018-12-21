# from src.features.pinghost import pinghost

def menu():
    print("Greetings! Welcome to the automated terminal command center. What can I do for you today?")
    print("")
    print("Available Commands:")
    availablecommands()
    print("")
    print("What would you like to select today?")


def availablecommands():
    # list commands with their respective numbers in dictionary below
    command = {'1': 'Ping current host',
               '2': 'Run Netstat on current host',
               '3': 'Run ARP on current host',
               '4': 'Run a trace route to a specific host',
               '5': 'Run Ipconfig on current host'}

    # properly formats dictionary into list so that it is shown nicely on the main menu
    list1 = []
    list2 = []
    for num in range(0, len(command.keys())):
        list1.append(list(command.keys())[num])

    for num in range(0, len(command.values())):
        list2.append(list(command.values())[num])

    for num in range (0, len(command)):
        print ('({0}) {1}'.format(str(list1[num]), str(list2[num])))



