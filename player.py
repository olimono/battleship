class Player:
    def __init__(self, player_name, board, is_ai: bool, ships_list:list):
        self.player_name = player_name
        self.board = board
        self.is_ai = is_ai
        self.ships_list = ships_list
        self.wrecked_ships = 0
