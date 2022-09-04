import constants
import battleship as bs
from main import game_prep

#IA testing

player_test_IA_name = "BIMO"

board2 = bs.Board(player_test_IA_name)
player2 = bs.Player(player_test_IA_name, board2, True)
player2_ships = [bs.Barco(**barco_dict) for barco_dict in constants.lista_barcos]
    
game_prep(player2_ships, player2) #una vez inicializados los barcos hay que decidir sus cordenadas y colocarlos