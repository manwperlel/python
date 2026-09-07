import random

number = random.randint(1, 30)
print(number)
number_user = 0
attempts = 5
cut = False
while cut == False:
    number_user = int(input("ingrese un numero:"))

    if number_user < number:
        attempts = attempts - 1
        print("el numero es mayor")
        print(f"te quedan {attempts} intentos")
        
    elif number_user > number:
        attempts = attempts - 1
        print("el numero es menor")
        print(f"te quedan {attempts} intentos")
    else:
        cut = True

    if attempts == 0:
        cut = True

if attempts > 0:
    print(f"ganaste! lo lograte en {attempts} intentos")
else:
    print(f"perdiste, el numero era {number}")