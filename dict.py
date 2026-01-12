# 1.
students_marks = {"prajwal": 89, "rohit": 2, "vijay": 56, "sanjay": 45, "yash": 34}
print(students_marks)

# 2.
print("The marks of prajwal is:", students_marks["prajwal"])

# 3.
students_marks["ram"] = 90
print(students_marks)

# 4.
students_marks["prajwal"] = 7
print(students_marks)

# 5.
del students_marks["ram"]
print(students_marks)

# 6.
print(students_marks.keys())

# 7.
print(students_marks.values())

# 8.
for student_name, marks in students_marks.items():
    print(f"{student_name} marks are: {marks}")

# 9.
print("Is prajwal in dictionary:", "prajwal" in students_marks)

# 10.
print("Is 46 in dictionary values:", 46 in students_marks.values())

# 11.
print("Marks of vijay using get():", students_marks.get("vijay"))

# 12.
employees_department = {
    "salmaan": "HR",
    "SRK": "Finance",
    "sanju": "cricket",
    "prajwal": "entc"
}

# 13.
print("Dept of sanju is:", employees_department["sanju"])

# 14.
employees_department["ram"] = "Marketing"
print(employees_department)

# 15.
employees_department["ram"] = "Sales"
print(employees_department)

# 16.
del employees_department["SRK"]
print(employees_department)

# 17. Sort employees by name (ascending)
print(dict(sorted(employees_department.items(), key=lambda x: x[0])))

# 18. Sort employees by department (ascending)
print(dict(sorted(employees_department.items(), key=lambda x: x[1])))

# 19. Sort employees by name (descending)
print(dict(sorted(employees_department.items(), key=lambda x: x[0], reverse=True)))

# 20. Sort employees by department (descending)
print(dict(sorted(employees_department.items(), key=lambda x: x[1], reverse=True)))

# 21.
print("Employees in cricket dept:",
      [name for name, dept in employees_department.items() if dept == "cricket"])

# 22.
count_above_80 = 0
for marks in students_marks.values():
    if marks > 80:
        count_above_80 += 1
print("Number of students scored above 80:", count_above_80)

# 23.
nested_student_details = {
    "prajwal": {"age": 20, "grade": "A", "department": "IT"},
    "yash": {"age": 21, "grade": "B", "department": "ENTC"},
    "harshal": {"age": 22, "grade": "C", "department": "MECH"}
}
print(nested_student_details)

# 24.
print("Grade of harshal is:", nested_student_details["harshal"]["grade"])

# 25.
nested_student_details["yash"]["grade"] = "O"
print("Updated grade of yash:", nested_student_details["yash"]["grade"])

# 26.
for student_name, details in nested_student_details.items():
    print(f"{student_name} scored grade: {details['grade']}")

# 27.
additional_students = {"rahul": 75, "deepak": 85}
students_marks.update(additional_students)
print(students_marks)

# 28.
additional_students.clear()
print("After clearing additional_students:", additional_students)

# 29.
students_marks_copy = students_marks.copy()
students_marks_copy["yash"] = 95
print("Original Dictionary:", students_marks)
print("Modified Copy:", students_marks_copy)

# 30.
number_squares = {}
for num in range(1, 6):
    number_squares[num] = num ** 2
print(number_squares)
