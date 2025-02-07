import os
from termcolor import colored
from ships import Ship

class Board():
    letters_list = ['A','B','C','D','E','F','G','H','I','J']
    numbers_list = ['0','1','2','3','4','5','6','7','8','9']

    def __init__(self, type):
        self.type = type
        self.board_coordinates_list = []
        self.board_coordinates_statuses_list = []
        for number in Board.numbers_list:
            for letter in Board.letters_list:
                self.board_coordinates_list.append(f"{letter}{number}")
        for coordinate in self.board_coordinates_list:
            coordinate_dict = {
                'coordinate': coordinate,
                'occupied': False, # coordinate's occupancy only matters for ship placement and when firing
                'status': "~" # ~ = not fired, O = miss, S = ship on X = hit
            }
            self.board_coordinates_statuses_list.append(coordinate_dict)
    
    def getCoordinateOccupancy(self, coordinate):
        coordinate_index = self.board_coordinates_list.index(coordinate)
        return self.board_coordinates_statuses_list[coordinate_index]['occupied']
    
    def getCoordinateStatus(self, coordinate):
        coordinate_index = self.board_coordinates_list.index(coordinate)
        return self.board_coordinates_statuses_list[coordinate_index]['status']

    def displayBoard(self):
        row_count = 0
        status_list_copy = self.board_coordinates_statuses_list.copy()
        print(colored(f"\n{self.type} Board:\n", "green"))
        print(f"  {' '.join(self.letters_list)}")

        def write_row(row_index):
            row_start_index = row_index *10
            return list(map(lambda coord: coord["status"],status_list_copy[row_start_index : row_start_index + 10]))

        while row_count < 10:
            row_string = " ".join(write_row(row_count))
            print(f"{row_count} {row_string}")
            row_count += 1
            

    

