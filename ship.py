from random import randint

class Ship:
    full_coords = []
    wrecked = False
    def __init__(self, length:int, boat_name:str, health:int):
        self.length = length
        self.full_coords = []
        self.boat_name = boat_name
        self.health = health
        self.start_coord = None
        self.is_vertical = None

    def ask_coords(self, is_ai:bool, board:object):
        '''
        pide las coordenadas para los barcos en el caso del jugador
        genera aleatoriamente las coordenadas de los barcos en el caso de la ia
        no estoy segura de que pedir el input directamente aquí sea lo mejor
        '''
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

    def __repr__(self):
        return self.boat_name

    @property
    def loose_health(self):
        '''
        método para perder salud cuando le disparan, si está a cero llama a hundir barco
        '''
        self.health -= 1
        if self.health == 0:
            self.sink_ship
    
    @property
    def sink_ship(self):
        '''
        metodo para cambiar estado a hundido
        '''
        self.wrecked = True
        print(f"{self.boat_name} sunk!")

