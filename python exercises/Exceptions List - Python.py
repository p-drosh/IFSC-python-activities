def zrdivision(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("It will not be any Zero division here.")
    except TypeError:
        print("It was not possible to do anything with these values.")

print(zrdivision (10, 2))