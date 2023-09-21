
for i in range(10):
    for j in range(i + 1, 10):
        if i == len(range(10))-2 and j > i:
            print("{}{}".format(i, j))

        else:
            print("{}{}".format(i, j), end=", ")
