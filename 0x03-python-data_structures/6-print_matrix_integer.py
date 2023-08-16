#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for row in matrix:
            for cell in row:
                print("{:d}".format(cell), end=" "if col != row[-1] else "")
            print()
