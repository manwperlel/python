number = int(input("Enter a number:"))
number2 = number % 2
while number > 0:
    if number2 == 0:
        print("The number is even:", number)
    elif number2 == 1:
        print("The number is odd:", number)
    number = number - 1
    number2 = number % 2