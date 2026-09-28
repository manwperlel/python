import random

deck = []
mano = []
colores = ("pica", "corazon", "trebol", "diamente")
dinero = 100
numeros_mano = []

def as_valor():
    print("te a salido un as, cuanto va a valer?")
    print("")

def new_carta ():
    number = random.randint(2, 11)

    if number == 11:
        as_valor()

    color = random.choice(colores)
    deck.append((color, number))
    mano.append((color, number))
    numeros_mano.append(number)

while True:
    try:
        apuesta = int(input("ingrese el total de la apuesta:"))
        if apuesta >= 1 and apuesta <= dinero:
            dinero = dinero - apuesta
            break
        else:
            print("VALOR INVALIDO")
    except ValueError:
        print("\n\nporfavor ingrese un numero valido\n")
        print(f"DINERO DISPLONIBLE: {dinero}")


print(f"\n\ndinero actual:{dinero}")
print(f"cantidad apostada:{apuesta}\n\n")


new_carta()
new_carta()

total = sum(numeros_mano)

print(f"mano actual:{mano}")

print(f"suma total de los valores es {total}\n\n")

while True:
    try:
            print("precione 1 para pedir una carta")
            print("precione 2 para finalizar la jugada\n")
            decision = int(input("tome una decision:"))
        
            if decision == 1:
                new_carta()
                print(f"\n\nmano actual:{mano}\n\n")
                total = sum(numeros_mano)
                print(f"suma total de los valores es {total}\n\n")
            elif decision == 2:
                break
            else:
                print("\n\n\n\nPORFAVOR INGRESE UN NUMERO VALIDO")
                print(f"\n\nmano actual:{mano}")
                print(f"suma total de los valores es {total}\n\n")
            if total > 21:
                print("perdiste")
                break
    except ValueError:
        print("\n\n\n\nPORFAVOR INGRESE UN NUMERO VALIDO")
        print(f"\n\nmano actual:{mano}")