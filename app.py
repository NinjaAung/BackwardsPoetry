import random
import os
from colorama import Fore, Back, Style






banner = '''
__________                                        
\______   \ _______  __ ___________  ______ ____  
 |       _// __ \  \/ // __ \_  __ \/  ___// __ \ 
 |    |   \  ___/\   /\  ___/|  | \/\___ \\  ___/ 
 |____|_  /\___  >\_/  \___  >__|  /____  >\___  >
        \/     \/          \/           \/     \/ 
'''

os. system('clear')
print("_" * 55 + Fore.BLUE + banner + Fore.RESET + "_" * 55)



def options():
    return


def main(poem):
    global lines
    lines = poem.split("\n")
    lines.reverse()

    for poem in lines:
        print(poem)
