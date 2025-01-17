import math
from coordinate import Coordinate

class Ship():
    letters_list = ['A','B','C','D','E','F','G','H','I','J']

    def __init__(self):
        self.ship_coordinates = []
        self.damage = 0
        self.placeShip()

    # Override in individual ship type classes
    def placeShip(self):
        coordinates = []
        while True:
            print(f"Place a {self.name} which has {self.post_count} posts and must be positioned vertically or horizontally (no diagonals).")
            for i in range(0,2):
                while True:
                    try:
                        coordinate = Coordinate()
                        coordinates.append(coordinate)
                        break
                    except Exception as e:
                        print(f"{e}...try again.")

            # If the following check is true, we know that the coordinates are valid format, and that the coordinates match the ship length and are in a proper orientation
            if self.isValidateShipLength(coordinates):
                print(f"These ship coordinates are valid and match the length of a {self.name}.")
                break
            else:
                print(f"Invalid coordinates for this ship. Please try again")
                coordinates = []

            # TODO:One more placement check must be made before breaking out of while loop to confirm that the ship coordinates do not overlap with another ship...this will come with board construction
        self.getAllShipCoordinates(coordinates)

    def isValidateShipLength(self, coordinate_list) -> bool:
        eucladian_points = []
        for i in range(0, len(coordinate_list)):
            coordinate_letter = str(coordinate_list[i])[0]
            coordinate_number = str(coordinate_list[i])[1]
            coordinate_letter_value = Ship.letters_list.index(coordinate_letter)
            eucladian_points.append((coordinate_letter_value, int(coordinate_number)))
        distance = math.dist(eucladian_points[0], eucladian_points[1])
        if self.post_count == distance + 1:
            return True
        else:
            return False
            
    
    def getAllShipCoordinates(self, coordinates:list):
        pass

    
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


