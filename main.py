import os
from termcolor import colored
import string
import math

# Define a class to represent a board
class Board:
    def __init__(self, playerName:str):
        self.playerName = playerName
        self.board = []
        self.board_size = 5
        self.board_spaces = 25
        self.head = "   A B C D E"
        self.createBoard()
        self.all_ship_coordinates = []
        self.damage_count = 0
        

    def __repr__(self):
        return f"{self.playerName}'s Board"
    
    def createBoard(self):
        """
            Creates a board with a size of 5x5. The board is a list of lists.
        """
        for i in range(0, self.board_spaces):
            self.board.append(' -')
    
    def displayBoard(self):
        """
            Displays the board in the CLI.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.playerName == "Computer":
            print(colored(self.__repr__(),'red'))
        else:
            print(colored(self.__repr__(), 'green'))
        print(f'\n{self.head}')
        for row in range(0, self.board_size):
            # More to do here.
            print(row, "".join(self.board[(row*5):(row*5)+5]))
        print(f'\n')

# Define a class to represent a ship
class Ship:
    def __init__(self, type:str, board:object):
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
        self.placeShip()
        for coord in self.ship_coordinates:
            board.all_ship_coordinates.append(coord)
        

    def __repr__(self):
        return f'The type of ship you selected is a {self.type} which has {self.post_num} posts.'
    
    def placeShip(self):
        """
            Places a ship by first asking user for desired ship coordinates, then assigning all coordinates included within that coordinate range.

            Parameters:
                none
            
            Returns:
                Adds coordinates to self.ship_coordinates
        """
        while True:
            coordinates = getShipCoordinates()
            is_valid_ship_coordinates = checkShipCoordinates(coordinates, self.post_num)
            if is_valid_ship_coordinates:
                # Insert all coordinates included between the two ends
                # Determine which character matches
                if coordinates[0][0] == coordinates[1][0]: # First character (letter) matches
                    static_first_character = coordinates[0][0]
                    initial_second_character = int(coordinates[0][1])
                    final_second_character = int(coordinates[1][1])
                    # This is only a partial solution. Won't include all coordinate numbers or the order in which they are given (i.e "A4" to "A0")
                    for num in range(initial_second_character,final_second_character+1):
                        # No need to worry about breaking bounds of board because checkShipCoordinates does this
                        self.ship_coordinates.append(f'{static_first_character}{num}')
                else:
                    allowed_letters = list(string.ascii_uppercase[:5])
                    static_second_character = coordinates[0][1]
                    initial_first_character_index = allowed_letters.index(coordinates[0][0])
                    final_first_character_index = allowed_letters.index(coordinates[1][0])
                    for index in range(initial_first_character_index,final_first_character_index+1):
                        self.ship_coordinates.append(f'{allowed_letters[index]}{static_second_character}')
                break
            else:
                print(colored('Coordinates are invalid for this ship', 'red'))
                continue

# FUNCTIONS THAT HANDLE COORDINATE VALIDATION (USED IN BOTH SHIP PLACEMENT AND ATTACKS)

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

# FUNCTIONS THAT HANDLE BOARD MANIPULATION

def commitFire(coordinate:str, target_board:object):
    """
        This function performs the firing action on a target board's coordinate. It determines if the attack was a hit or miss and updates the board accordingly.

        Parameters:
            : str : coordinate - the location attacked
            : object: target_board - the board being attacked
        
        Returns:
            Displays the target board with updated hit or miss.

    """
    allowed_letters = list(string.ascii_uppercase[:5])
    allowed_ints = ["0", "1", "2", "3", "4"]
    coordinate_list = []
    for integer in allowed_ints:
        for letter in allowed_letters:
            coordinate_list.append(f'{letter}{integer}')
    board_index = coordinate_list.index(coordinate)
    target_board.board[board_index] = " X"
    # The code below will be uncommented once the system for checking targets is complete
    if attackBattleReport(coordinate, target_board):
        target_board.board[board_index] = " X"
        target_board.damage_count += 1
    else:
        target_board.board[board_index] = " O"

def attackBattleReport(coordinate:str, target_board:object):
    if coordinate in target_board.all_ship_coordinates:
        return True
    else:
        return False

def requestFire(target_board:object):
    while True:
        attack_coordinates = input("Enter coordinates to fire on: ")
        if validateCoordinate(attack_coordinates):
            commitFire(attack_coordinates,target_board)
            target_board.displayBoard()
            break
        else:
            print(colored("You entered invalid coordinates. Please provide valid coordinates.", "red"))


# TESTING BOARD
c_board = Board("Computer")
c_battleship = Ship("battleship",c_board)
c_carrier = Ship("carrier", c_board)
print(f'All ship coordinates on computer board: {c_board.all_ship_coordinates}')
requestFire(c_board)
print(f'All ship coordinates on computer board: {c_board.all_ship_coordinates}')
requestFire(c_board)



# TESTING SHIPS
""" f_carrier = Ship("carrier")
print(f_carrier)
f_carrier.placeShip() """

""" f_battleship = Ship("battleship")
print(f_battleship)
f_battleship.placeShip()
print(colored(f'The new ship coordinates are: {f_battleship.ship_coordinates}','green')) """

""" f_cruiser = Ship("cruiser")
print(f_cruiser)
f_cruiser.placeShip()

f_submarine = Ship("submarine")
print(f_submarine)
f_submarine.placeShip() """

