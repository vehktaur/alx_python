def fibonacci_sequence(n):
    fib_list = []

    for index in range(n):
        if len(fib_list) == 0:
            fib_list.append(index)
        elif len(fib_list) == 1:
            fib_list.append(index)
        else:
            fib_list.append(fib_list[index-1] + fib_list[index-2])
    return fib_list


# print(fibonacci_sequence(1))
