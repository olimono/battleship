
class Board:
    vertical_axis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    horizontal_axis = range(1, 10)
    matrix = []
    matrix_line = []
    
    def __init__(self, player):
        self.player = player
        for n in self.horizontal_axis:
            matrix_line = [str(n) + l for l in self.vertical_axis]
            self.matrix.append(matrix_line)

    def __repr__(self) -> str:
        #metodo repr del objeto Board
        title_subline = "  -----------  "
        header_row = "  "
        for l in self.vertical_axis:
            header_row += l + "  "
        lines_to_print = ""
        for row in self.matrix:
            line_to_print = str(self.matrix.index(row)+1)
            for self.position in row:
                line_to_print += " - "
            lines_to_print += line_to_print + "\n"
        
        return "\n Mapa Jugadora " + self.player + "\n" + title_subline + "\n" + header_row + "\n" + lines_to_print

board = Board("oli")
print(board)