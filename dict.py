

# 1. 
dict_stu = {"prajwal": 89, "jay": 2, "vijay": 56, "sanjay": 45, "yash": 34}
print(dict_stu)

# 2. 
print("The marks of prajwal is:", dict_stu["prajwal"])

# 3. 
dict_stu["ram"] = 90
print(dict_stu)

# 4. 
dict_stu["prajwal"] = 7
print(dict_stu)

# 5. 
del dict_stu["ram"]
print(dict_stu)

# 6. 
print(dict_stu.keys())

# 7.
print(dict_stu.values())

# 8. 
for key, value in dict_stu.items():
    print(f"{key} marks are: {value}")

# 9. 
print("Is prajwal in dictionary:", "prajwal" in dict_stu)

# 10. 
print("Is 90 in dictionary values:", 90 in dict_stu.values())

# 11. 
print("Marks of vijay using get():", dict_stu.get("vijay"))

# 12. 
dict_emp = {"ajay": "HR", "vijay": "Finance", "sanjay": "IT", "yash": "IT"}

# 13. 
print("Dept of yash is:", dict_emp["yash"])

# 14. 
dict_emp["ram"] = "Marketing"
print(dict_emp)

# 15. 
dict_emp["ram"] = "Sales"
print(dict_emp)

# 16. 
del dict_emp["vijay"]
print(dict_emp)

# 17. Sort employees by name (ascending)
print(dict(sorted(dict_emp.items(), key=lambda x: x[0])))

# 18. Sort employees by department (ascending)
print(dict(sorted(dict_emp.items(), key=lambda x: x[1])))

# 19. Sort employees by name (descending)
print(dict(sorted(dict_emp.items(), key=lambda x: x[0], reverse=True)))

# 20. Sort employees by department (descending)
print(dict(sorted(dict_emp.items(), key=lambda x: x[1], reverse=True)))

# 21. 
print("Employees in IT dept:", [k for k, v in dict_emp.items() if v == "IT"])

# 22. 
cnt = 0
for value in dict_stu.values():
    if value > 80:
        cnt += 1
print("Number of students scored above 80:", cnt)

# 23. 
dict_nested = {
    "ajay": {"age": 20, "grade": "A", "department": "IT"},
    "vijay": {"age": 21, "grade": "B", "department": "ENTC"},
    "sanjay": {"age": 22, "grade": "C", "department": "MECH"}
}
print(dict_nested)

# 24. 
print("Grade of ajay is:", dict_nested["ajay"]["grade"])

# 25. 
dict_nested["ajay"]["grade"] = "O"
print("Updated grade of ajay:", dict_nested["ajay"]["grade"])

# 26. 
for key, value in dict_nested.items():
    print(f"{key} scored grade: {value['grade']}")

# 27. 
dict_stu2 = {"rahul": 75, "deepak": 85}
dict_stu.update(dict_stu2)
print(dict_stu)

# 28. 
dict_stu2.clear()
print("After clearing dict_stu2:", dict_stu2)

# 29. 
dict_stu_copy = dict_stu.copy()
dict_stu_copy["ajay"] = 95
print("Original Dictionary:", dict_stu)
print("Modified Copy:", dict_stu_copy)

# 30. 
dict_squares = {}
for i in range(1, 6):
    dict_squares[i] = i ** 2
print(dict_squares)
