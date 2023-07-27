#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    def double(item):
        return item * number
    new_list = list(map(double, my_list))
    return new_list
