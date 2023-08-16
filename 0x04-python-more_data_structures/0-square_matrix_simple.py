#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for rows in matrix:
        squared_rows = []
        for items in rows:
            squared_rows.append(items ** 2)
        squared_matrix.append(squared_rows)
    return squared_matrix
