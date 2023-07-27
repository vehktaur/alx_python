#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary or a_dictionary is None:
        return None
    else:
        values = a_dictionary.values()
        values = list(values)
        values.sort()
        return values[-1]
