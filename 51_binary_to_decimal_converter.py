potencia = 0
binario =[]
total = 0

while True:
    number = input("Enter a binary number: ").strip()

    
    es_valido = True
    for caracter in number:
        if caracter != "0" and caracter != "1":
            es_valido = False
            break 

    if es_valido and len(number) > 0:
        break
    else:
        print("Error: Ingresá únicamente números binarios (0 y 1). Reintentá.\n")

for i in number:
    if i == "1":
        binario.append(1)
    elif i == "0":
        binario.append(0)


binario.reverse()

for i in binario:
    total= total +(i * 2 ** potencia)
    potencia = potencia + 1

print(total)