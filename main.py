import regex
import os
import time
from termcolor import colored
from coordinate import *
from ships import *
from boards import *
from turn import *
from actions import *


def main():
    clearScreen()
    print("Welcome to Terminal Battleships!\n")
    print('''\n
                    ____
                 ___|__|___    __
           _____|__________|__|__
           \                    /
            \   USS WINSTON    /
             \________________/
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    \n
    ''')
    print("\nIf you're brave enough, its time to enter the wide ocean and engage in your favorite game of (digital) naval combat.\n")
    try:
        while True: 
            home_menu_selection = input("[1] Begin game\n[2] Read instructions\n[3] Quit\n: ")
            
            if home_menu_selection == "1":
                clearScreen()
                player_1_hits = 0
                player_2_hits = 0
                player_turn = 1
                # Create boards and instantiate ships
                p1s_board, p1t_board, p2s_board, p2t_board = Board("Player 1 Ships"), Board("Player 1 Targeting"), Board("Player 2 Ships"), Board("Player 2 Targeting")
                player_ship_boards = [p1s_board, p2s_board]
                player_number = 1
                for player_board in player_ship_boards:
                    print(colored(f"Starting ship deployment for Player {player_number}", "green"))
                    player_board.displayBoard()
                    Carrier(player_board)
                    clearScreen()
                    player_board.displayBoard()
                    Battleship(player_board)
                    clearScreen()
                    player_board.displayBoard()
                    Cruiser(player_board)
                    clearScreen()
                    player_board.displayBoard()
                    Submarine(player_board)
                    clearScreen()
                    player_board.displayBoard()
                    Destroyer(player_board)
                    clearScreen()
                    player_board.displayBoard()
                    input("\nRemember your ship placement as this will be the last time such secret information will be displayed. Press enter to continue...")
                    if player_number == 1:
                        clearScreen()
                        print(f"You have 10 seconds to pass the controls over to Player 2 for ship deployment...")
                        time_count = 10
                        while time_count > 0:
                            if time_count % 5 == 0:
                                print(f"{time_count} seconds remaining...")
                            time.sleep(1.0)
                            time_count -= 1
                    clearScreen()
                    player_number = 2
                while player_1_hits != 17 and player_2_hits != 17:
                    clearScreen()
                    print(f"Current score:\n\nPlayer 1 hits: {player_1_hits}\nPlayer 2 hits: {player_2_hits}\n")
                    input("Press enter to continue...")
                    if player_turn == 1:
                        player_1_hits = Turn(p2s_board, p1t_board, player_1_hits).hits
                        player_turn = 2
                    elif player_turn == 2:
                        player_2_hits = Turn(p1s_board, p2t_board, player_2_hits).hits
                        player_turn = 1
                if player_1_hits == 17:
                    print(colored("\nPlayer 1 sank all of Player 2's ships and wins!\n", "green"))
                else:
                    print(colored("\nPlayer 2 sank all of Player 1's ships and wins!\n", "green"))
                end_game_choice = input(f'If you\'d like to quit, type "q" and then hit enter, otherwise hit enter to continue. ')
                end_game_choice = end_game_choice.lower()
                if end_game_choice == "q":
                    clearScreen()
                    break
                else:
                    clearScreen()
                    continue
            elif home_menu_selection == "2":
                if os.name == 'nt':
                    # Read instructions on Windows...
                    os.system("more ./docs/instructions.txt")
                else:
                    #... on macOS or Linux
                    os.system("less ./docs/instructions.txt")
                    clearScreen()
            elif home_menu_selection == "3":
                clearScreen()
                print(colored("See you next time Captain!", "green"))
                break
            else:
                clearScreen()
                print(colored("Please select a menu item listed below\n", "red"))
    except KeyboardInterrupt:
        clearScreen()
        print("You quit the game. See you next time!")



if __name__ == "__main__":
    main()