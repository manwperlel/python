palabra = input("escriba su palabra:").lower()
vocales = 0

for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vocales += 1

print(f"su palabra tiene {vocales} vocales")