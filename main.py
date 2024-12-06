import os
from termcolor import colored
import string
import math

class Ship:
    def __init__(self, type:str):
        self.type = type
        match self.type:
            case "carrier":
                self.post_num = 4
            case "battleship":
                self.post_num = 3
            case "cruiser":
                self.post_num = 2
            case "submarine":
                self.post_num = 1
        
        self.ship_coordinates = []
        


    def __repr__(self):
        return f'The type of ship you selected is a {self.type} which has {self.post_num} posts.'
    
    def placeShip(self):
        while True:
            coordinates = getShipCoordinates()
            is_valid_ship_coordinates = checkShipCoordinates(coordinates, self.post_num)
            if is_valid_ship_coordinates:
                # Insert all coordinates included between the two ends
                print(coordinates)
                # Determine which character matches
                if coordinates[0][0] == coordinates[1][0]: # First character (letter) matches
                    static_first_character = coordinates[0][0]
                    initial_second_character = int(coordinates[0][1])
                    for index in range(0,self.post_num):
                        # Pick back up here in adding coordinates to the ship placement
                        pass
                break
            else:
                print(colored('Coordinates are invalid for this ship', 'red'))
                continue



def validateCoordinate(coordinate:str) -> bool:
    allowed_letters = list(string.ascii_uppercase[:5])
    allowed_ints = ["0", "1", "2", "3", "4"]
    # Rules
    #    1. Coordinate must contain only 2 characters
    #    2. The first character must be an uppercase letter between A-J
    #    3. The second character must be a number between 0-9

    # Rule 1
    if len(coordinate) != 2:
        print(colored("Coordinates must be two characters long.","red"))
        return None
    
    # Rule 2
    try:
        allowed_letters.index(coordinate[0])
    except ValueError:
        print(colored("The first coordinate character must be a letter between A-E.","red"))
        return None
    
    # Rule 3
    try:
        allowed_ints.index(coordinate[1])
    except ValueError:
        print(colored("The second coordinate character must be a number between 0-4.", 'red'))
        return None
    
    return True

# Define a function to get ship coordinates
def getShipCoordinates():
    shipCoordinates = []
    while len(shipCoordinates) < 2:
        coordinate = input("Enter a coordinate: ")
        valid = validateCoordinate(coordinate)
        if valid:
            shipCoordinates.append(coordinate)
            continue
        else:
            continue
    return shipCoordinates

def checkShipCoordinates(coordinates:list, ship_posts:int) -> bool:
    """
        Checks the distance between two coordinates and compares it to the number of posts for a ship. This is an important step in confirming ship placement at the start of the game.

        Parameters:
        : list : coordinates - raw coordinate strings passed from CLI during getShipCoordinates

        Return:
        : bool: True if the distance matches number of posts for a ship, False if it does not.
    """
    values_dict = {"A":0,"B":1,"C":2,"D":3,"E":4,"0":0,"1":1,"2":2,"3":3,"4":4}

    # Transform "coordinates" parameter into two separate coordinates
    coordinate1,coordinate2 = list(coordinates[0]), list(coordinates[1])

    # Make sure that at least one of the positional characters match across the coordinates, then proceed to find the distance
    if (coordinate1[0] == coordinate2[0]) or (coordinate1[1] == coordinate2[1]):
        # The following nested for loops translate the coordinate strings into individual numbered 
        for coordinate in [coordinate1,coordinate2]:
            for index in range(0,2):
                key = coordinate[index]
                coordinate[index] = values_dict[key]
        # Find the distance between the two translated coordinates (plus 1 to make inclusive)
        distance = math.dist(coordinate1,coordinate2) + 1
        if distance == ship_posts:
            return True
        else:
            print(colored('There is a mismatch between distance and the number of ship posts.', 'red'))
            return False

    else:
        print(colored('Ships can only be placed horizontally or vertically; diagonal is not allowed. Please enter new coordinates'))

        #continue

f_carrier = Ship("carrier")
print(f_carrier)
f_carrier.placeShip()