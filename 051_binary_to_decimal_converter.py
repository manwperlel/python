power = 0
binary = []
total = 0

while True:
    number = input("Enter a binary number: ").strip()

    is_valid = True
    for character in number:
        if character != "0" and character != "1":
            is_valid = False
            break

    if is_valid and len(number) > 0:
        break
    else:
        print("Error: Enter binary numbers only (0 and 1). Try again.\n")

for i in number:
    if i == "1":
        binary.append(1)
    elif i == "0":
        binary.append(0)

binary.reverse()

for i in binary:
    total = total + (i * 2 ** power)
    power = power + 1

print(total)