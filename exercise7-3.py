def is_even(my_number):
    if my_number == 0:
        return "ʕ ಡ ﹏ ಡ ʔ"
    elif my_number % 2 == 0:
        return True
    else:
        return False

print(is_even(2))
print(is_even(5))
print(is_even(-10))
print(is_even(11))
print(is_even(0))
