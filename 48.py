counter = 0
suma = 0
cut = False
promedio = 0

while cut == False:
    number2 = float(input("enter a number"))
    if number2 > 0:
        counter = counter + 1
        suma = suma + number2
    elif number2 < 0:
        print(f"el numero {number2} es menor a 0")
    else:
        cut = True

promedio = (suma / counter)
print(promedio)