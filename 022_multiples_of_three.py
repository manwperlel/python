number = int(input("Enter a number:"))
counter = 0
residuo = 0
while counter < number:
    counter = counter + 1
    residuo = counter % 3
    if residuo == 0:
        print(counter)