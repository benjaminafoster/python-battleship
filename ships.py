""" Defines all characteristics and behaviors for the ships that populate the game board.

Ships are integral to this game as they are the targets for opposing players. Each board will contain five ships upon game initiation. Each player/computer has a carrier (5 posts), battleship (4 posts), cruiser (3 posts), submarine (3 posts), and a destroyer (2 posts) to place and fire upon during the game.

"""
import math
from termcolor import colored
from coordinate import Coordinate

class Ship():
    """Defines the ship class.

    This is the parent class for all ship subtypes. All ship coordinate validation takes place during object initialization. The one validation that does not occur is determining whether or not any of the ship's coordinates are already taken on the board. This process is started in get_board_availability that references board.coordinate_dict for space availability.

    Args:
        None
    
    Returns:
        A ship placed on the game board defined by boards.py. 
    """
    letters_list = ['A','B','C','D','E','F','G','H','I','J']

    def __init__(self):
        self.ship_coordinates = []
        self.damage = 0
        self.placeShip()

    # Override in individual ship type classes
    def placeShip(self):
        coordinates = []
        while True:
            print(colored(f"Place a {self.name} which has {self.post_count} posts and must be positioned vertically or horizontally (no diagonals).", 'blue'))
            for i in range(0,2):
                while True:
                    try:
                        coordinate = Coordinate()
                        coordinates.append(str(coordinate))
                        break
                    except Exception as e:
                        print(f"{e}...try again.")

            # If the following check is true, we know that the coordinates are valid format, and that the coordinates match the ship length and are in a proper orientation
            
            if self.isValidateShipLength(coordinates):
                print(colored(f"These ship coordinates are valid and match the length of a {self.name}.", 'green'))
                break
            else:
                print(colored(f"Invalid coordinates for this ship. Please try again", 'red'))
                coordinates = []

        self.getAllShipCoordinates(coordinates)

    def isValidateShipLength(self, coordinate_list) -> bool:
        eucladian_points = []
        for i in range(0, len(coordinate_list)):
            coordinate_letter = coordinate_list[i][0]
            coordinate_number = coordinate_list[i][1]
            coordinate_letter_value = Ship.letters_list.index(coordinate_letter)
            eucladian_points.append((coordinate_letter_value, int(coordinate_number)))
        distance = math.dist(eucladian_points[0], eucladian_points[1])
        if self.post_count == distance + 1:
            return True
        else:
            return False
            
    
    def getAllShipCoordinates(self, coordinates:list):
        if coordinates[0][0] == coordinates[1][0]:
            # First, find the reference coordinate (lowest number value) to set lower bound to for iterative coordinate append
            min_so_far = float("inf")
            reference_coordinate = None
            for coord in coordinates:
                if int(coord[1]) < min_so_far:
                    min_so_far = int(coord[1])
                    reference_coordinate = coord
            letter, number = list(reference_coordinate)
            # Walk up the number value for each coordinate and append to the ship_coordinates variable
            for i in range(0, self.post_count):
                new_num = int(number) + i
                self.ship_coordinates.append(f"{letter}{str(new_num)}")

        elif coordinates[0][1] == coordinates[1][1]:
            # Convert letters from both coordinates to their number values; set min_so_far
            min_so_far = float("inf")
            reference_coordinate = None
            for coord in coordinates:
                coord_letter_index = Ship.letters_list.index(coord[0])
                if coord_letter_index < min_so_far:
                    min_so_far = coord_letter_index
                    reference_coordinate = f"{str(coord_letter_index)}{coord[1]}"
            letter_value, number = list(reference_coordinate)
            for i in range(0, self.post_count):
                new_letter_value = int(letter_value) + i
                self.ship_coordinates.append(f"{str(Ship.letters_list[new_letter_value])}{number}")

        print(self.ship_coordinates)
    
class Carrier(Ship):
    def __init__(self):
        self.name = "carrier"
        self.post_count = 5
        super().__init__()

class Battleship(Ship):
    def __init__(self):
        self.name = "battleship"
        self.post_count = 4
        super().__init__()

class Cruiser(Ship):
    def __init__(self):
        self.name = "cruiser"
        self.post_count = 3
        super().__init__()

class Destroyer(Ship):
    def __init__(self):
        self.name = "destroyer"
        self.post_count = 2
        super().__init__()

class Submarine(Ship):
    def __init__(self):
        self.name = "submarine"
        self.post_count = 3
        super().__init__()


