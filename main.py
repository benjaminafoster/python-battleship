import os
from termcolor import colored
import string

class Ship:
    def __init__(self, type:str):
        self.type = type
        match self.type:
            case "carrier":
                self.post_num = 5
            case "battleship":
                self.post_num = 4
            case "cruiser":
                self.post_num = 3
            case "submarine":
                self.post_num = 3
            case "destroyer":
                self.post_num = 2

    def placeShip(self, ship_coordinates:list):
        # Create a list of available coordinate letters
        list_of_letters = list(string.ascii_uppercase[:10])

def validateCoordinate(coordinate:str) -> bool:
    allowed_letters = list(string.ascii_uppercase[:10])
    allowed_ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
        print(colored("The first coordinate character must be a letter between A-J.","red"))
        return None
    
    # Rule 3
    try:
        allowed_ints.index(coordinate[1])
    except ValueError:
        print(colored("The second coordinate character must be a number between 0-9.", 'red'))
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
