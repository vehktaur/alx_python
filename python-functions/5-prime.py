def is_prime(number):
    test_prime = 0

    for num in range(2, number+1):
        if number % num == 0:
            test_prime += 1

    if number < 1 or type(number) is not int or test_prime > 1:
        return False

    return True
