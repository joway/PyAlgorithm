def matrix_col_sum(matrix, col):
    result = 0
    for row in matrix:
        result += row[col]
    return result
