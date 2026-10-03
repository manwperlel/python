import random

"variables, listas"

deck = []
mano = []
mano_dealer = []
colores = ("pica", "corazon", "trebol", "diamante")
carta_figura_random = [10, "J", "Q", "K"]
dinero = 100
numero_mano = []
numero_mano_dealer = []
jugadas = 2



"======================================================================================================================"
"====================================================  FUNCIONES  ====================================================="
"======================================================================================================================"

def dealer_carta():
    while True:
        number = random.randint(2, 11)
        color = random.choice(colores)

        carta_dealer = (color, number)

        if number == 10:
                    figura = carta_figura()
                    carta_dealer = (color, figura)
                    print(figura)

        if carta_dealer not in deck:
            break

    deck.append(carta_dealer)
    mano_dealer.append(carta_dealer)
    numero_mano_dealer.append(number)

def new_carta ():
    while True:
        number = random.randint(2, 11)
        color = random.choice(colores)

        carta = (color, number)

        if number == 10:
            figura = carta_figura()
            carta = (color, figura)
            print(figura)

        if carta not in deck:
            break

    deck.append(carta)

    if number == 11:
        number = as_valor()
        carta = (color, number)

    mano.append(carta)
    numero_mano.append(number)

def carta_figura():
    figura = random.choice(carta_figura_random)
    print(figura)
    return figura


def as_valor():
    while True:
        try:
            print("TE SALIO UN AS!")
            print("cuanto va a valer?")
            print("presione 1 para que valga 1")
            print("presione 2 para que valga 11\n\n")


            as_elegir_valor = int(input("elegir valor:"))

            if as_elegir_valor == 1:
                number = 1
                return number

            elif as_elegir_valor == 2:
                number = 11
                return number

            else:
                print("\n\nporfavor ingrese un numero valido\n")


        except ValueError:
            print("\n\nporfavor ingrese un numero valido\n")



"======================================================================================================================"
"====================================================  JUEGO  ========================================================="
"======================================================================================================================"

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
        print(f"DINERO DISPONIBLE: {dinero}")


print(f"\n\ndinero actual:{dinero}")
print(f"cantidad apostada:{apuesta}\n\n")


new_carta()
new_carta()
dealer_carta()

total = sum(numero_mano)
total_dealer = sum(numero_mano_dealer)

print(f"mano actual:{mano}")
print(f"suma total de los valores es {total}\n")
print(f"mano del dealer:{mano_dealer}")
print(f"suma total del delaer:{total_dealer}\n\n")


"TOMAR DECISION"

while True:
    try:
            print("precione 1 para pedir una carta")
            print("precione 2 para finalizar la jugada\n")
            decision = int(input("tome una decision:"))

            if decision == 1:
                new_carta()
                print(f"\n\nmano actual:{mano}\n\n")
                total = sum(numero_mano)
                print(f"suma total de los valores es {total}\n\n")
                jugadas = jugadas + 1
                print(f"jugadas totales:{jugadas}")

            elif decision == 2:
                break

            else:
                print("\n\n\n\nPORFAVOR INGRESE UN NUMERO VALIDO")
                print(f"\n\nmano actual:{mano}")
                print(f"suma total de los valores es {total}\n\n")

            if total > 21:
                break

    except ValueError:
        print("\n\n\n\nPORFAVOR INGRESE UN NUMERO VALIDO")
        print(f"\n\nmano actual:{mano}")


"dealer juego"

while True:
    if total > 21:
        break

    elif total_dealer <= 16:
        dealer_carta()
        total_dealer = sum(numero_mano_dealer)

    else:
        break

print(f"\n\n\n\n\n\n\n\nmano actual del dealer:{mano_dealer}")
print(f"suma total del delaer:{total_dealer}\n\n")


"resultado"

if total > 21:
    print("perdiste")
    print(f"dinero final:{dinero}")

elif total_dealer > 21:
    print("ganaste")
    print(f"dinero apostado:{apuesta}")
    dinero = (dinero + apuesta * 2)
    print(f"dinero final:{dinero}")

elif total_dealer > total:
    print("perdiste")
    print(f"dinero final:{dinero}")

elif total_dealer < total:
    print("ganaste")
    print(f"dinero apostado:{apuesta}")
    dinero = (dinero + apuesta * 2)
    print(f"dinero final:{dinero}")

else:
    print("empate")
    dinero = dinero + apuesta



print("GRACIAS POR JUGAR")