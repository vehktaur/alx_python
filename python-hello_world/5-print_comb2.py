range_length = 200

for x in range(range_length):
    if x == len(range(range_length))-1:
        print("{:02}".format(x))
    else:
        print("{:02},".format(x), end=" ")
