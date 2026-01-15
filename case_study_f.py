n = int(input("Enter the number of days for which attendance is recorded: "))

dict_stu = {}

for i in range(n):
    students = set(input(f"Enter students present on day{i} : ").split(","))
    dict_stu[f"day{i}"] = students

print(dict_stu)

dict_count_day = {}
for students in dict_stu.values():
    for student in students:
        dict_count_day[student] = dict_count_day.get(student, 0) + 1

print(dict_count_day)

present_all_days = []
absent_at_least_one_day = []

for student, count in dict_count_day.items():
    if count == n:
        present_all_days.append(student)
    else:
        absent_at_least_one_day.append(student)

print("present all days:", present_all_days)
print("absent at least one day:", absent_at_least_one_day)

all_students = set()
for students in dict_stu.values():
    all_students.update(students)

print("Unique students across all days:", all_students)
