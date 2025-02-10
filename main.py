import regex
import os
import time
from termcolor import colored
from coordinate import *
from ships import *
from boards import *
from actions import *


def main():
    clearScreen()
    print("Welcome to Terminal Battleships!\n")
    print("\nIf you're brave enough, its time to enter the wide ocean and engage in your favorite game of (digital) naval combat.\n")
    while True: 
        print("[1] Begin game")
        print("[2] Quit")
        home_menu_selection = input(": ")
        
        if home_menu_selection == "1":
            # Create boards and instantiate ships
            p1s_board, p1t_board, p2s_board, p2t_board = Board("Player 1 Ships"), Board("Player 1 Targeting"), Board("Player 2 Ships"), Board("Player 2 Targeting")
            player_ship_boards = [p1s_board, p2s_board]
            player_number = 1
            for player_board in player_ship_boards:
                print(colored(f"Starting ship deployment for Player {player_number}", "green"))
                Carrier(player_board)
                Battleship(player_board)
                Cruiser(player_board)
                Submarine(player_board)
                Destroyer(player_board)
                if player_number == 1:
                    print(f"You have 10 seconds to pass the controls over to Player 2 for ship deployment...")
                    time_count = 10
                    while time_count > 0:
                        if time_count % 5 == 0:
                            print(f"{time_count} seconds remaining...")
                        time.sleep(1.0)
                        time_count -= 1
                clearScreen()
                player_number += 1
            p1s_board.displayBoard()
            p2s_board.displayBoard()
        elif home_menu_selection == "2":
            clearScreen()
            print(colored("See you next time Captain!", "green"))
            break
        else:
            clearScreen()
            print(colored("Please select a menu item listed below\n", "red"))



if __name__ == "__main__":
    main()