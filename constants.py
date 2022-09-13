welcome_message = "Welcome to Hundir la Flota. In this adventure, you will have 5 ships,\
each with a different lenght. \n Now you will have to place your ships. Each time, \
you will be asked for one starting coord and after that, you will have to choose \
whether the boat is vertical or horizontal and the boat will be atumatcally \
placed. If you place the boat in such a way that it crashes with a wall,\
don't worry, you will be asked for the starting coord again so you can\
place it correctly. Good luck!"

board_horizontal_axis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
board_vertical_axis = range(1, 10)

lista_barcos = [
        {
            "length": 5, 
            "boat_name":"carrier", 
            "health": 5,
            }, 
            {
            "length": 4, 
            "boat_name":"battleship", 
            "health": 4,
            }, 
            {
            "length": 3, 
            "boat_name":"cruiser", 
            "health": 3,
            }, 
            {
            "length": 3, 
            "boat_name":"submarine", 
            "health": 3,
            }, 
            {
            "length": 2, 
            "boat_name":"destructor", 
            "health": 2,
            }
            ]

