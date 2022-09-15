from Board import *
from Ship import *
import pytest

# if __name__ == '__main__':
#     time.sleep(1)
#     game = bs.Game()
#     player1_name = "oli"
#     game.start_game(player1_name)
#     #while game.winner == None:
#     game.turn(game.player1, game.player2)
#     #game.turn(game.player2, game.player2)

player_name = "Test name"

def test_empty_board():
    empty = Board(player_name)
    assert empty != None