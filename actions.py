from termcolor import colored
from boards import *
from coordinate import *

def fire(board):
    print(colored("You've selected to fire on a target.", "blue"))
    coordinate = str(Coordinate())
    coordinate_status = board.getCoordinateStatus(coordinate)
    match coordinate_status:
        case "S":
            print(colored("HIT!", "red"))
            coordinate_index = board.board_coordinates_list.index(coordinate)
            board.board_coordinates_statuses_list[coordinate_index]["status"] = "X"
        case _:
            print(colored("Miss...", "blue"))
