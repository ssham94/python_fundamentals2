def convert_to_c(fahrenheit):
    fahrenheit = int(fahrenheit)
    c = (fahrenheit-32) * (5/9)
    return "{} Fahrenheit is {:.2f} Celcius".format(fahrenheit, c) # Making sure that celcius only comes out in two decimal places

print(convert_to_c(79))
print(convert_to_c(60))
print(convert_to_c(32))
print(convert_to_c("56"))
print(convert_to_c("98"))