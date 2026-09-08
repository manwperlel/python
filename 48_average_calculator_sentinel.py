counter = 0
addition = 0
cut = False
average = 0

while cut == False:
    number2 = float(input("enter a number:"))
    if number2 > 0:
        counter = counter + 1
        addition = addition + number2
    elif number2 < 0:
        print(f"The number {number2} is less than 0.")
    else:
        cut = True

average = (addition / counter)
print(average)