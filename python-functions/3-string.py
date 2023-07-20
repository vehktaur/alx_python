def reverse_string(string):
    reversed = ""
    for char in string:
        reversed = char + reversed
    return reversed

# def reverse_string(string):
#     reversed=""
#     for char in string:
#         reversed = "{}{}".format(char,reversed)
#     return reversed

# def reverse_string(string):
#     reversed = ""
#     index = 1
#     for letter in string:
#         reversed += string[-index]
#         index += 1
#     return reversed

# print(reverse_string("competition"))
