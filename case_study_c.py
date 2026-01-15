n = int(input("Enter the Number of Students to Enroll: "))

dict = {}

for i in range(n):
    name = input("Enter student name: ")
    courses = tuple(input("Enter courses (comma separated): ").split(","))
    dict[name] = courses

print(dict)

for name, courses in dict.items():
    if "Data Science" in courses and "AI" in courses:
        print(name)

all_courses = set()
for courses in dict.values():
    all_courses.update(courses)

print(all_courses)

course_count = {}
for courses in dict.values():
    for c in courses:
        course_count[c] = course_count.get(c, 0) + 1

no_repeat = [course for course, count in course_count.items() if count == 1]

print(course_count)
print(no_repeat)
