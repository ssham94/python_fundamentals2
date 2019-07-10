def wrap_text(my_word, my_symbols):
    return "{}{}{}".format(my_symbols, my_word, my_symbols[::-1])

print(wrap_text("hello", "!_+_="))
print(wrap_text("food please", "!!!==="))
print(wrap_text("its cold in here", "==++!!"))