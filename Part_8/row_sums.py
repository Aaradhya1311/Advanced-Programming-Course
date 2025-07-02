my_matrix = [[1, 2], [3, 4]]

def row_sums(matrix):
    total_r1 = 0
    total_r2 = 0
    for x in range(2):
        total_r1 = my_matrix[0][x-1] + total_r1
        total_r2 = my_matrix[1][x-1] + total_r2
    my_matrix[0].append(total_r1)
    my_matrix[1].append(total_r2)
    return my_matrix

row_sums(my_matrix)
print(my_matrix)