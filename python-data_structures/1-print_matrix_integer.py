#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for list_item in list:
            print("{:d}".format(list_item), end=" ")
        else:
            print()

