import constants
from player import *
from board import *
from ship import *
  
class Board:
    horizontal_axis = constants.board_horizontal_axis
    vertical_axis = constants.board_vertical_axis
    
    def __init__(self, player):
        self.player = player
        self.water_full = []
        self.matrix_line = []
        self.matrix = []
        self.accepted_coords = []
        self.shot_ship = []
        self.shot_water = []


        for n in self.vertical_axis:
            self.matrix_line = [str(n) + l for l in self.horizontal_axis]
            self.matrix.append(self.matrix_line)
        for line in self.matrix:
            for coord in line:
                self.accepted_coords.append(str(coord))

    def __repr__(self) -> str:
        title_subline = "  -----------  "
        header_row = "  "
        for l in self.horizontal_axis:
            header_row += l + "  "
        lines_to_print = ""
        for row in self.matrix:
            line_to_print = str(self.matrix.index(row)+1)
            for element in row:
                if element in self.water_full:
                    line_to_print += " o "
                else:
                    line_to_print += " ~ "
            lines_to_print += line_to_print + "\n"
        return "\n Mapa jugadora " + self.player + "\n" + title_subline + "\n" + header_row + "\n" + lines_to_print

    def place_ship(self, boat:Barco):
        """
        to full the water the places where to print the boats
        """
        full_coords = [] #aquí se colocarán las coordenadas completas del barco
        for row in self.matrix:
            if boat.start_coord in row:
                index_column = row.index(boat.start_coord)
                try: #se comprueba que las coordenadas completas no se salen del tablero, si se salen, se vuelve a empezar en game prep
                    for n in range(boat.length):
                        if boat.is_vertical == True:
                            full_coords.append(self.matrix[self.matrix.index(row) + n][index_column])
                        else:
                            full_coords.append(self.matrix[self.matrix.index(row)][index_column + n])
                except:
                    full_coords = []
                                        
        for coord in full_coords:
            #testing
            print(coord, self.water_full) 
            #comprueba que no haya otro barco en esa posición
            if coord in self.water_full:
                full_coords = []

        if full_coords != []:
            for coord in full_coords:
                self.water_full.append(coord)
            boat.full_coords = full_coords        

    def oponent_board(self):
        title_subline = "  -----------  "
        header_row = "  "
        for l in self.horizontal_axis:
            header_row += l + "  "
        lines_to_print = ""
        for row in self.matrix:
            line_to_print = str(self.matrix.index(row)+1)
            for element in row:
                if element in self.shot_ship:
                    line_to_print += " x "
                elif element in self.shot_water:
                    line_to_print += " ~ "
                else:
                    line_to_print += " - "
            lines_to_print += line_to_print + "\n"
        return print("\n Mapa oponente " + self.player + "\n" + title_subline + "\n" + header_row + "\n" + lines_to_print)