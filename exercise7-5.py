def convert_to_c(fahrenheit):
    fahrenheit = int(fahrenheit)
    c = (fahrenheit-32) * (5/9)
    return "{} Fahrenheit is {:.2f} Celcius".format(fahrenheit, c)

print(convert_to_c(79))
print(convert_to_c(60))
print(convert_to_c(32))
print(convert_to_c("56"))
print(convert_to_c("98"))