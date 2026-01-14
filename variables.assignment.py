
# 1. Write a program to demonstrate how a local variable inside a function 
# works and is not accessible outside the function.
def local_demo():
    x_local = "I exist only inside"
    print(f"Inside function: {x_local}")

# 2. Subtotal: 2420, Tax: 121.0, Discount: 242.0, Total: 2299.0, Payment: UPI 
# Create a function that defines a global variable inside it using the global keyword and modify its value.
payment_type = "None"
def set_payment():
    global payment_type
    payment_type = "UPI"
    subtotal, tax, discount = 2420, 121.0, 242.0
    total = subtotal + tax - discount
    print(f"Subtotal: {subtotal}\nTax: {tax}\nDiscount: {discount}\nTotal: {total}\nPayment: {payment_type}")

# 3. Write a program where a global variable is updated by multiple function calls using the global keyword.
global_counter = 0
def update_counter():
    global global_counter
    global_counter += 10

# 4. Create two functions where both use a global variable to calculate and store cumulative total sales.
total_sales = 0
def register_online_sale(amt):
    global total_sales
    total_sales += amt
def register_instore_sale(amt):
    global total_sales
    total_sales += amt

# 5. Write a nested function where the inner function accesses an enclosing variable from the outer function.
def outer_access():
    msg = "Enclosing Variable"
    def inner_access():
        print(f"Inner accessed: {msg}")
    inner_access()

# 6. Demonstrate the use of nonlocal keyword by modifying an enclosing variable inside an inner function.
def outer_nonlocal():
    val = 10
    def modify():
        nonlocal val
        val += 5
    modify()
    return val

# 7. Create a nested function structure with three levels and print variables from local, enclosing, and global scopes.
g_var = "Global"
def level_1():
    e_var = "Enclosing"
    def level_2():
        l_var = "Local"
        print(f"Levels: {g_var} -> {e_var} -> {l_var}")
    level_2()

# 8. Write a function where local variable shadows a global variable and show both outputs.
shadow = "Global Value"
def shadow_demo():
    shadow = "Local Value"
    print(f"Inside (Local): {shadow}")

# 9. Create a program to show how Python searches variable names using the LEGB rule.
def legb_test():
    # L=Local, E=Enclosing, G=Global, B=Built-in (like len)
    def inner():
        print(f"Built-in len() check: {len([1,2,3])}")
    inner()

# 10. Write a function to show that local variables are destroyed after function execution ends.
def destruction_demo():
    temp_var = "I am temporary"
    return temp_var

# 11. Create a nested function where both inner and outer functions take arguments and print their values.
def outer_args(a):
    def inner_args(b):
        print(f"Outer arg: {a}, Inner arg: {b}")
    inner_args(20)

# 12. Write a nested function that calculates total marks using an outer function for input and an inner function for computation.
def marks_manager(scores):
    def compute():
        return sum(scores)
    print(f"Total Marks: {compute()}")

# 13. Demonstrate how enclosing variable stores the running total for a counter function using nonlocal.
def running_total_counter():
    count = 0
    def add(n):
        nonlocal count
        count += n
        return count
    return add

# 14. Write a closure function that generates a multiplier and demonstrate how the enclosing variable remembers state.
def multiplier_factory(n):
    def multiply(x):
        return x * n
    return multiply

# 15. Create a function with variable positional arguments (*args) to calculate the sum of all given numbers.
def sum_args(*args):
    return sum(args)

# 16. Write a function with variable positional arguments that finds the maximum value from all numbers passed.
def find_max(*args):
    return max(args)

# 17. Create a function with variable keyword arguments (**kwargs) that displays student details.
def student_info(**kwargs):
    for k, v in kwargs.items(): print(f"{k}: {v}")

# 18. Write a function using variable keyword arguments to print employee records with department and salary.
def emp_record(**kwargs):
    print(f"Dept: {kwargs.get('dept')}, Salary: {kwargs.get('salary')}")

# 19. Combine *args and **kwargs in a single function and print both values separately.
def mixed_args(*args, **kwargs):
    print(f"Positional: {args}, Keywords: {kwargs}")

# 20. Write a function that uses *args to calculate average sales for any number of branches.
def avg_sales(*sales):
    return sum(sales) / len(sales) if sales else 0

# 21. Write a function that uses **kwargs to configure a model with learning_rate and epochs.
def config_model(**kwargs):
    print(f"Rate: {kwargs.get('learning_rate')}, Epochs: {kwargs.get('epochs')}")

# 22. Create a nested function that uses *args in the inner function to calculate total of passed values.
def math_wrapper():
    def adder(*args):
        return sum(args)
    return adder

# 23. Write a program where outer function accepts employee details and inner function calculates bonus based on salary.
def employee_portal(salary):
    def calc_bonus():
        return salary * 0.10
    print(f"Bonus: {calc_bonus()}")

# 24. Demonstrate how a nonlocal variable can be used to maintain the count of calls to a nested function.
def call_tracker():
    calls = 0
    def track():
        nonlocal calls
        calls += 1
        print(f"Call number: {calls}")
    return track

# 25. Write a program to show how global and local variables can have same name but store different data.
data = "Global Data"
def same_name_demo():
    data = [1, 2, 3] # Local list
    print(f"Local: {data}")

# 26. Create a nested function example where inner function modifies enclosing variable to accumulate expenses.
def expense_manager():
    total_exp = 0
    def add_exp(amt):
        nonlocal total_exp
        total_exp += amt
        print(f"Accumulated Expense: {total_exp}")
    return add_exp

# 27. Write a function that uses *args to concatenate multiple strings into a single string.
def join_words(*args):
    return " ".join(args)

# 28. Create a function that uses **kwargs to print formatted key value pairs as system configuration.
def print_config(**kwargs):
    for k, v in kwargs.items(): print(f"SYS_{k.upper()}={v}")

# 29. Write a function with both *args and **kwargs to simulate order details (items and prices).
def process_order(*items, **details):
    print(f"Customer: {details.get('name')}, Items: {items}")

# 30. Design a nested function where outer function provides base salary and inner function adds incentives using nonlocal.
def salary_calculator(base):
    def add_incentives(bonus):
        nonlocal base
        base += bonus
        return base
    return add_incentives

print("--- Result 2 ---")
set_payment()
print("\n--- Result 8 ---")
shadow_demo()
