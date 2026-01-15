stu_data = {}

for i in range(5):
    day = input("Enter the day: ")
    names = set(input(f"Enter the names of students present on {day} : ").split(","))
    stu_data[day] = names

print(stu_data)

stu_present_days = {}

for students in stu_data.values():
    for student in students:
        stu_present_days[student] = stu_present_days.get(student, 0) + 1

print(stu_present_days)

present_all_days = [student for student, count in stu_present_days.items() if count == 5]
print(f"The student list present for all days: {present_all_days}")

absent_at_least_one_day = [student for student, count in stu_present_days.items() if count != 5]
print(f" absent for at least one day: {absent_at_least_one_day}")

all_students = set()
for students in stu_data.values():
    all_students.update(students)

print(f"The total number of students : {len(all_students)}: {all_students}")
