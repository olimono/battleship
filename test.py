start_coord = "a"
matrix = [["a", "b", "c","h"],["j","k","l","s"], ["1","2","3","4"]]
water_full = []
is_vertical = True
#to full the water the places where to print the boats 
for row in matrix:
    if start_coord in row:
        index_column = row.index(start_coord)
        for n in range(3):
            if is_vertical == True:
                water_full.append(matrix[matrix.index(row) + n][index_column])
            else:
                water_full.append(matrix[matrix.index(row)][index_column + n])
print(water_full)


# para print los barcos 
# for self.column in row:
#   if matrix[linea][column] not in water_full:
#       line_to_print += " - "
#   else:
#       line_to_print += " x "    


# para almacenar water_full:
# water_full =+ 