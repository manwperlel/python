print("======================================================================")
print("============================= { DIE } ================================")
print("======================================================================\n\n\n")

limit = int(input("Enter a limit: "))
counter = 0


side1 = 0
side2 = 0
side3 = 0
side4 = 0
side5 = 0
side6 = 0

while counter < limit:
    counter = counter + 1
    number = int(input(f"Roll number {counter}: "))


    if number < 1 or number > 6:
        print("Invalid number. Must be between 1 and 6.")
        counter = counter - 1 
        if number == 1:
            side1 = side1 + 1
        elif number == 2:
            side2 = side2 + 1
        elif number == 3:
            side3 = side3 + 1
        elif number == 4:
            side4 = side4 + 1
        elif number == 5:
            side5 = side5 + 1
        elif number == 6:
            side6 = side6 + 1


average_side1 = (side1 / limit) * 100
average_side2 = (side2 / limit) * 100
average_side3 = (side3 / limit) * 100
average_side4 = (side4 / limit) * 100
average_side5 = (side5 / limit) * 100
average_side6 = (side6 / limit) * 100

print("======================================================================")
print("============================= { RESULT } =============================")
print("======================================================================")

print(f"\nSide 1: {average_side1}%")
print(f"Side 2: {average_side2}%")
print(f"Side 3: {average_side3}%")
print(f"Side 4: {average_side4}%")
print(f"Side 5: {average_side5}%")
print(f"Side 6: {average_side6}%")