number = 163
number2 = 0
cut = "not"
while cut == "not":
    number2 = int(input("Enter a number:"))
    if number2 < number:
        print("The number is greater")
    elif number2 > number:
        print("The number is smaller")
    elif number2 == number:
        cut = "yes"

print("You won!")