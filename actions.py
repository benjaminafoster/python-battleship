from termcolor import colored
from boards import *
from coordinate import *
from playaudio import playaudio

'''def fire(enemy_board, friendly_targeting_board):
    print(colored("You've selected to fire on a target.", "blue"))
    coordinate = str(Coordinate())
    coordinate_status = enemy_board.getCoordinateStatus(coordinate)
    match coordinate_status:
        case "S":
            print(colored("HIT!", "red"))
            coordinate_index = enemy_board.board_coordinates_list.index(coordinate)
            enemy_board.board_coordinates_statuses_list[coordinate_index]["status"] = "X"
            friendly_targeting_board.board_coordinates_statuses_list[coordinate_index]["status"] = "X"
        case "~":
            print("Miss")
            coordinate_index = enemy_board.board_coordinates_list.index(coordinate)
            enemy_board.board_coordinates_statuses_list[coordinate_index]["status"] = "O"
            friendly_targeting_board.board_coordinates_statuses_list[coordinate_index]["status"] = "O"

        case _:
            print("Coordinate already guessed. No effect.")'''

def playSound(sound):
    if sound == "hit":
        playaudio("./assets/explosion_sound.mp3")
    elif sound == "miss":
        playaudio("./assets/splash_sound.mp3")
    else:
        pass

def clearScreen():
    if os.name == 'nt':
        # Clear command for Windows...
        os.system('cls')
    else:
        #... for macOS or Linux
        os.system('clear')
