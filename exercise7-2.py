def negative(my_number):
    if my_number > 0:
        return False
    elif my_number < 0:
        return True
    else:
        return "¯\_(ツ)_/¯"

print(negative(5))
print(negative(-1))
print(negative(-4))
print(negative(25))
print(negative(0))