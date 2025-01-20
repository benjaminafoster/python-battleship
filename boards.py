from ships import Ship

class Board():
    letters_list = ['A','B','C','D','E','F','G','H','I','J']
    numbers_list = ['0','1','2','3','4','5','6','7','8','9']

    def __init__(self):
        self.board_coordinates_list = []
        self.board_coordinates_statuses_list = []
        for number in Board.numbers_list:
            for letter in Board.letters_list:
                self.board_coordinates_list.append(f"{letter}{number}")
        for coordinate in self.board_coordinates_list:
            coordinate_dict = {
                'coordinate': coordinate,
                'occupied': False, # if a ship is placed on this coordinate, this attribute will be updated
                'status': 0 # 0 = not fired, 1 = miss, 2 = hit
            }
            self.board_coordinates_statuses_list.append(coordinate_dict)
        # print(self.board_coordates_statuses_list)

    def createBoard(self):
        """ Called at start of game to walk through adding ships to the board.

        Args:
            None

        Returns:
            None -- Ships with valide coordinates and don't overlap are placed on the board, with coodinate statuses updated accordingly in self.board_coordinates_statuses_list
        
        """
        ship_type_list = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
        pass
    
    def getCoordinateStatus(self, coordinate):
        coordinate_index = self.board_coordinates_list.index(coordinate)
        return self.board_coordinates_statuses_list[coordinate_index]['status']

    

