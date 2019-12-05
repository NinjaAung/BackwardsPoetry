import random
import os
from colorama import Fore, Back, Style



mypoem = '''The Moving Finger writes; and, having writ, Moves on:
nor all thy Piety nor Wit. Shall lure it back to cancel half a Line, 
Nor all thy Tears wash out a Word of it.'''




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

def lines_printed(lines):

    lines.reverse()
    print(Fore.RED + "\nReversed ----> \n" + Fore.RESET)

    for poem in lines:
            print(Fore.BLUE + poem + "\n" + Fore.RESET)

    print(Fore.RED + "Mixed up ----> \n" + Fore.RESET)
    lines_printed_random(lines)

def main(option, poem):
    if option == "1":
        num_line = 1
        line_num = int(input("How many lines do you have: "))
        line = []
        
        while line_num > 0:
            line.append(input(f'{num_line}. '))
            num_line += 1
            line_num -= 1
        print()

        for poem_c in line:
            print(poem_c)

        lines_printed(line)

        
            
    elif option == "2":
        poem_name = input("\nName of the file with ext. (example.txt): ")
        print()

        poem_file = open(poem_name, "r")
        poem_lines = poem_file.readlines()

        with open(poem_name, 'r') as fin:
            print(fin.read())
        
        lines_printed(poem_lines)
        
    elif option == "3":
        print()
        print(poem + "\n")


        lines = poem.split("\n")
        lines_printed(lines)


    else:
        print("That's not a option goodbye")



main(choice, mypoem)