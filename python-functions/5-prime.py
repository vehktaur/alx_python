def is_prime(number):
    test_prime = 0

    for num in range(1, number+1):
        if number % num == 0:
            test_prime += 1

    if number < 1 or type(number) is not int or test_prime > 2:
        return False
    print(test_prime)
    return True

print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))