def accesslist (lis, index):
    try:
        return lis[index]
    except IndexError:
        return "Error: Index outside the range."
    except TypeError:
        return "Error: Invalid Index."
    
print(accesslist ([10, 20, 30], 5))