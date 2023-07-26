#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    for list in matrix:
        i = 0
        for list_item in list:
            if i == len(list) - 1:
                print("{:d}".format(list_item))
            else:
                print("{:d}".format(list_item), end=" ")
            i += 1
