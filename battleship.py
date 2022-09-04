from random import randint, random


class Barco:
    full_coords = []
    wrecked = False
    def __init__(self, length:int, boat_name:str, health:int):
        self.length = length
        self.full_coords = []
        self.boat_name = boat_name
        self.health = health
        self.start_coord = None
        self.is_vertical = None

    #def get_coords(self, start_coord, is_vertical):
    #    self.start_coord = start_coord
    #    self.is_vertical = is_vertical


    def ask_coords(self, is_ai:bool, board:object):
        vertical_axis_index = None
        horizontal_axis_index = None
        if is_ai:
            vertical_axis_index = randint(0,8)
            horizontal_axis_index = randint(0,9)
            print(vertical_axis_index, horizontal_axis_index)
            self.start_coord = str(board.vertical_axis[vertical_axis_index]) + str(board.horizontal_axis[horizontal_axis_index]) 
            is_vertical_boool = randint(0,1)
            print(is_vertical_boool)
            self.is_vertical = bool(is_vertical_boool)

        else:
            while self.start_coord == None:
                self.input_coord = input(f"Now let's place your {self.boat_name}. It has {self.length} lenght. Enter its start coords (example 1A):")
                if str(self.input_coord) in board.accepted_coords:
                    self.start_coord = self.input_coord
                else:
                    print("Oh, snap! seems like you have introduced a wrong coord. Remember to input first the number and second the letter.")
            while self.is_vertical == None:
                self.input_is_vertical = input("Now would you like to place it vertical or horizontal?")
                if self.input_is_vertical.upper() in ["VERTICAL", "V", "HORIZONTAL", "H"]:
                    self.is_vertical = self.input_is_vertical
                else:
                    print("Oh, snap! seems like you have introduced a wrong coord. Remember to input V for vertical or H for horizontal.")
            if self.is_vertical.upper() in ["VERTICAL", "V"]:
                self.is_vertical = True
            elif self.is_vertical.upper() in ["HORIZONTAL", "H"]:
                self.is_vertical = False
        

      
class Board:
    horizontal_axis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    vertical_axis = range(1, 10)
    matrix = []
    matrix_line = []
    water_full = []
    accepted_coords = []
    
    def __init__(self, player):
        self.player = player
        for n in self.vertical_axis:
            matrix_line = [str(n) + l for l in self.horizontal_axis]
            self.matrix.append(matrix_line)
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
                    line_to_print += " x "
                else:
                    line_to_print += " - "
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

        #boat.assign_coords(full_coords)

class Player:
    def __init__(self, player_name, board, is_ai: bool, ships_list=None):
        self.player_name = player_name
        self.board = board
        self.is_ai = is_ai
        if ships_list == None:
            self.ships_list = []
        else:
            self.ships_list = ships_list


#print(board_player.place_ship(bs_player))
#board_player.place_ship(cruiser_player)

#print(carrier_player.full_coords)

#def check_ship_place():
#   while carrier_is_vertical == ""
#       try:
#           carrier_is_vertical in accepted_values_hv 
#       except:
#           raise ValueError
#           carrier_is_vertical = ""
#           print("It must be a value between x and x")



