#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new_matrix = []
    for inner_matrix in matrix:
        new_inner_matrix = []
        for inner_item in inner_matrix:
            new_inner_matrix.append(inner_item ** 2)
        new_matrix.append(new_inner_matrix)

    return new_matrix
