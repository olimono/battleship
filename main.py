import time
import battleship as bs
import constants

def game_prep(player_ships:list, player:object):
        for ship in player_ships:
            ship.get_coords(player.is_ai, player.board)
            board.place_ship(ship)
            print(player.board)
            player1.ships_list.append(ship)


if __name__ == '__main__':
    player1_name = input("Welcome to Hundir la Flota. Please enter a name for player one and hit enter. ")
    time.sleep(0.5)
    print(f"Hi, {player1_name} Let's place your ships! \n")    
    time.sleep(1)
    board = bs.Board(player1_name)
    player1 = bs.Player(player1_name, board, False)
    player1_ships = [bs.Barco(**barco_dict) for barco_dict in constants.lista_barcos]
    print(board)

    game_prep(player1_ships, player1)

    player2_name = "BIMO"
    board2 = bs.Board(player2_name)
    player2 = bs.Player(player2_name, board2, True)
    player2_ships = [bs.Barco(**barco_dict) for barco_dict in constants.lista_barcos]
    
    game_prep(player2_ships, player2)


    print("¡Empieza el juego!")