def long_word(my_word):
    if len(my_word) < 8:
        return False
    else:
        return True

print(long_word("helloworld"))
print(long_word("hello"))
print(long_word("im hungry")) #It includes the space
print(long_word("ardvark"))
print(long_word("timetoeat"))