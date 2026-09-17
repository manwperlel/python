# Technical vocabulary: GPA / Average grade, Attendance, and Failed subjects
gpa = float(input("Enter your average grade (GPA): "))
attendance = int(input("Enter your attendance percentage (%): "))
failed_courses = int(input("How many failed courses do you have?: "))

# Scholarship validation logic
if gpa < 8.5:
    print("We cannot grant you the scholarship (GPA is too low).")
elif attendance < 80:
    print("We cannot grant you the scholarship (Attendance is too low).")
elif failed_courses >= 2:
    print("We cannot grant you the scholarship (Too many failed courses).")
else:
    print("Congratulations! You have been awarded the scholarship!")