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
print('''
would you like to:
1. Input your poem directly in
2. Read from a file
3. Read the poem already in the code
''')
choice = input("Choose a number 1 - 3: ")



def main(option):
    if option == "1":
        print("not available yet")
    elif option == "2":
        print("asd")
    elif option == "3":
        print("dsa")
    else:
        print("That's not a option goodbye")




    # global lines
    # lines = poem.split("\n")
    # lines.reverse()

    # for poem in lines:
    #     print(poem)



main(choice)