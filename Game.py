from random import randint
import time
import constants
from Player import *
from Board import *
from Ship import *

class Game:
    def __init__(self):
        self.winner = None

    def game_prep(self, player_ships:list, player:object):
        '''
        gestiona toda la preparación del juego
        obtener las coordenadas de los barcos y colocarlos
        el while controla que full_coords no esté vacía, si está vacía es que se han colocado mal y se ha vaciado en el último paso
        '''
        print(player_ships)
        for ship in player_ships:
            while ship.full_coords == []:
                ship.ask_coords(player.is_ai, player.board)
                player.board.place_ship(ship) 
            print(player.board)
            time.sleep(1)


    def start_game(self, player1_name):
        '''
        inicializa los objetos player, board y barcos y lanza el método game prep
        '''
        print(constants.welcome_message)
        time.sleep(1)
        player1_name = player1_name
        time.sleep(0.5)
        print(f"Hi, {player1_name} Let's place your ships! \n")    
        time.sleep(1)
        self.board1 = Board(player1_name)
        player1_ships = [Ship(**barco_dict) for barco_dict in constants.lista_barcos]
        self.player1 = Player(player1_name, self.board1, False, player1_ships)
        self.game_prep(player1_ships, self.player1)

        player2_name = "BIMO"
        self.board2 = Board(player2_name)
        player2_ships = [Ship(**barco_dict) for barco_dict in constants.lista_barcos]
        self.player2 = Player(player2_name, self.board2, True, player2_ships)
        self.game_prep(player2_ships, self.player2)
        
        print("¡Empieza el juego!")

    def shoot_ship(self, player:Player, oponent:Player, oponent_board:Board, coord: str= None):
        
        if player.is_ai == False:
            coord = input("Insert coordinate to shoot. (eg. 1A)")
        else:
            vertical_axis_index = randint(0,8)
            horizontal_axis_index = randint(0,9)
            print(vertical_axis_index, horizontal_axis_index)
            coord = str(oponent_board.vertical_axis[vertical_axis_index]) + str(oponent_board.horizontal_axis[horizontal_axis_index]) 

        if coord in oponent_board.water_full:
            oponent_board.shot_ship.append(coord)
            print(oponent_board.shot_ship)
            for ship in oponent.ships_list:
                if coord in ship.full_coords:
                    ship.loose_health
        else:
            oponent_board.shot_water.append(coord)
            print(oponent_board.shot_water)
    
    def turn(self, player:Player, oponent:Player, oponent_board:Board):
        self.shoot_ship(player, oponent, oponent_board)
        time.sleep(1)
        oponent_board.oponent_board()
        if oponent.wrecked_ships == 5:
            self.winner = player
            self.end_game()