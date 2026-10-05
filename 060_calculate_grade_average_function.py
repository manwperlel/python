def calculate_grade_average(class_grades):
    return sum(class_grades) / len(class_grades)

class_grades = [1, 5, 8, 6]

result = calculate_grade_average(class_grades)

print(result)