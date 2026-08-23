number1 = int(input("Enter a number:"))

number2 = 0
result = 0

if number1 < 0:
    print("Invalid number:")

while number2 < number1:
    number2 = number2 + 1
    print(number2)
    result = result + number2
    print("result:", result)