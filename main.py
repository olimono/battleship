import time
import battleship as bs
from player import *
from board import *
from ship import *


if __name__ == '__main__':
    time.sleep(1)
    game = bs.Game()
    player1_name = input("Please enter your name and hit enter. ")
    game.start_game(player1_name)
    while game.winner == None:
        game.turn(game.player1, game.player2, game.board2)
        game.turn(game.player2, game.player2, game.board1)
