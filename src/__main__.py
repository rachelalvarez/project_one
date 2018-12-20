from src.features.mainmenu import *
from src.features.pinghost import *

mainmenu.menu()
userinput = input()

if userinput == "1":
    pinghost.pinghost()