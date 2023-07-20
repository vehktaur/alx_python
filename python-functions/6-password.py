def validate_password(password):
    is_upper = False
    is_digit = False
    is_spaced = False

    for char in password:
        if char == " ":
            is_spaced = True
        if char.isupper():
            is_upper = True
        if char.isdigit():
            is_digit = True

    if is_spaced or not is_upper or not is_digit:
        return False
    else:
        return True

# print(validate_password("Password 123"))
