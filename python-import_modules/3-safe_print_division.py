#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = float(a/b)
        return result
    except:
        return "Types are not compatible"
    finally:
        return "Inside result: {}".format(result)


if __name__ == "__main__":
    safe_print_division()
