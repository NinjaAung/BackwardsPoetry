import random
import os
from colorama import Fore, Back, Style



mypoem = '''
The Moving Finger writes; and, having writ, Moves on:
nor all thy Piety nor Wit. Shall lure it back to cancel half a Line, 
Nor all thy Tears wash out a Word of it.
'''




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



def lines_printed_random(words):
    '''will randomly select lines from a list of strings and print them out in random order. 
    Repeats are okay and the number of lines printed should be equal to the original number of lines in the poem'''
    random_lines = len(words)
    for i in range(len(words)):
        line_index = random.randint(1, random_lines-1)
        print(words[line_index] + "\n")




def main(option, poem):
    if option == "1":
        print("not available yet")
    elif option == "2":
        print("asd")
    elif option == "3":

        print(poem + "\n")
        print(Fore.RED + "Reversed ----> \n" + Fore.RESET)

        lines = poem.split("\n")
        lines.reverse()

        for poem in lines:
            print(poem + "\n")

        print(Fore.RED + "Mixed up ----> \n" + Fore.RESET)
        lines_printed_random(lines)


    else:
        print("That's not a option goodbye")








main(choice, mypoem)