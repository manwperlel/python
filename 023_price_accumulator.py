price = 0
total = 0
cut = "not"
while cut == "not":
    price  = int(input("ingrese un precio:"))
    total = total + price

    if price == 0:
        cut = "yes"

print("The total is:", total)