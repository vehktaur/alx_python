#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary or a_dictionary is None:
        return None
    else:
        values = a_dictionary.values()
        values = list(values)
        values.sort()
        best_score = values[-1]
        high_scorer = ""

        for key, value in a_dictionary.items():
            if value == best_score:
                high_scorer = key
            else:
                continue
        return high_scorer
