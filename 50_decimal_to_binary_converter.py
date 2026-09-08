resto = 0
binary_digits = []
while True:
    try:
        number = int(input("Enter a positive integer:"))
        if number >= 0:
            break
        else:
            print("Please enter a non-negative number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if number == 0:
        binary_digits.append(0)


while number > 0:
    resto = number % 2
    number = number // 2
    binary_digits.append(resto)

binary_digits.reverse()
print(binary_digits)