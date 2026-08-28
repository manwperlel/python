grades = [5, 4, 2, 5, 6, 7, 4]
total_sum = 0

for grade in grades:
    total_sum += grade

average = total_sum / len(grades)

if average >= 7:
    print(f"You passed with an average of {average}")
else:
    print(f"You failed with an average of {average}")