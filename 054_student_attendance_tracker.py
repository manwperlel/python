student_list = {}

while True:
    student_name = input("Insert the student's name:")

    if student_name == "0":
        break

    present = input("Is the student present?:")

    student_list.update({student_name: present})

for student, present in student_list.items():
    print(f"{student}: {present}")
print(student_list)