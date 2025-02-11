import time
from termcolor import colored
from boards import *
from coordinate import *
from actions import *

class Turn():
    def __init__(self, enemy_board, targeting_board, player_hits):
        self.hits = player_hits
        clearScreen()
        targeting_board.displayBoard()
        while True:
            player_turn_selection = input("Do you want to [f]ire or [s]urrender your turn? ")
            player_turn_selection = player_turn_selection.lower()
            if player_turn_selection == "f":
                turn_status = 1
                while turn_status and self.hits != 17:
                    clearScreen()
                    targeting_board.displayBoard()
                    try:
                        turn_status = self.fire(enemy_board, targeting_board)
                        if turn_status == 1: # if turn status is still 1 after firing, that means a hit ocurred
                            self.hits += 1
                    except ValueError as e:
                        print(f"{e}...Try again.")
                clearScreen()
                print(f"You missed and now have 10 seconds to pass the controls over to the other player...")
                time_count = 10
                while time_count > 0:
                    if time_count % 5 == 0:
                        print(f"{time_count} seconds remaining...")
                    time.sleep(1.0)
                    time_count -= 1
                break
            elif player_turn_selection == "s":
                break
            else:
                print(colored("Invalid selection. Try again...", "red"))
                continue
        
    
    def fire(self, enemy_board, targeting_board): 
        print(colored("You've selected to fire on a target.", "blue"))
        coordinate = str(Coordinate())
        coordinate_status = enemy_board.getCoordinateStatus(coordinate)
        match coordinate_status:
            case "S":
                print(colored("HIT!", "red"))
                coordinate_index = enemy_board.board_coordinates_list.index(coordinate)
                enemy_board.board_coordinates_statuses_list[coordinate_index]["status"] = "X"
                targeting_board.board_coordinates_statuses_list[coordinate_index]["status"] = "X"
                return 1
            case "~":
                print("Miss")
                coordinate_index = enemy_board.board_coordinates_list.index(coordinate)
                enemy_board.board_coordinates_statuses_list[coordinate_index]["status"] = "O"
                targeting_board.board_coordinates_statuses_list[coordinate_index]["status"] = "O"
                return 0

            case _:
                print("Coordinate already guessed. No effect.")
                return 0
        
