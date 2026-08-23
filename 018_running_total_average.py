number1 = int(input("Enter a number:"))

number2 = 0
result = 0
grand_total = 0 
if number1 <= 0:
    print("Invalid number")
else:
    while number2 < number1:
        number2 = number2 + 1
        result = result + number2
        grand_total = grand_total + result
        print("result:", result)
average = grand_total / number1
print("sum result:", grand_total)
print("your average is:", average)