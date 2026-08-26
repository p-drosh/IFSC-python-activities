def strconv():
    inpt = int(input("Type a number: "))
    try:
        num = int(inpt)
    except ValueError:
        print("Error: invalid entry. Type another Number: ") 
    else:
        print(f" Converted Number: {num} ")
    finally:
        print("Conversion attempt concluded: ")
strconv()

