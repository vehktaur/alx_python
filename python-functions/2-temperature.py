def convert_to_celsius(fahrenheit):

    celsius = (5/9) * (fahrenheit - 32)

    if fahrenheit == -459.67:
        return round(celsius, 2)
    else:
        return celsius
