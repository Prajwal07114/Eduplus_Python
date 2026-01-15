

# Take number of employees
n = int(input("Enter the number of employees: "))

dict_emp = {}

# Input employee names and skills
for i in range(n):
    name = input("Enter employee name: ")
    skills = input("Enter skills (comma separated): ").lower().split(",")
    dict_emp[name] = skills

print("\nEmployee Dictionary:")
print(dict_emp)


# Display employees who know BOTH Python and SQL
#
print("\nEmployees who know both Python and SQL:")
for key, value in dict_emp.items():
    if "python" in value and "sql" in value:
        print(key)


# Find unique skills across all employees

unique_skills = set()
for value in dict_emp.values():
    unique_skills.update(value)

print("\nUnique skills across all employees:")
print(unique_skills)

# Employees sharing at least one skill with user input

num_skills = int(input("\nEnter number of skills to check: "))

user_skills = []
for i in range(num_skills):
    user_skills.append(input("Enter skill: ").lower())

count = 0
print("\nEmployees sharing at least one skill:")
for key, value in dict_emp.items():
    for skill in user_skills:
        if skill in value:
            print(key)
            count += 1
            break

print("Total employees matching:", count)
