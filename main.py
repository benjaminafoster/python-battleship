import regex
import os
from coordinate import *
from ships import *

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("Welcome to Terminal Battleships!\n")
        print("\nIf you're brave enough, its time to enter the wide ocean and engage in your favorite game of (digital) naval combat.\n")
        print("[1] Begin game")
        print("[2] Quit")
        home_menu_selection = input(": ")
        
        if home_menu_selection == "1":
            carrier = Carrier()
            battleship = Battleship()
            cruiser = Cruiser()
            submarine = Submarine()
            destroyer = Destroyer()    
        elif home_menu_selection == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("See you next time Captain!")
            break
        else:
            print("Please select a menu item listed above")



if __name__ == "__main__":
    main()