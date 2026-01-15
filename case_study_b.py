n1 = int(input("Enter the no of products in warehouse 1: "))
n2 = int(input("Enter the no of products in warehouse 2: "))

warehouse1 = {}
warehouse2 = {}

for i in range(n1):
    product_id = int(input("Enter product ID: "))
    product_name = input("Enter product name: ")
    product_quantity = int(input(f"Enter quantity of {product_name}: "))
    warehouse1[product_id] = (product_name, product_quantity)

for i in range(n2):
    product_id = int(input("Enter product ID: "))
    product_name = input("Enter product name: ")
    product_quantity = int(input(f"Enter quantity of {product_name}: "))
    warehouse2[product_id] = (product_name, product_quantity)

print(warehouse1)
print(warehouse2)

set1 = {value[0] for value in warehouse1.values()}
set2 = {value[0] for value in warehouse2.values()}

print(set1, set2)
print(set1.intersection(set2))
print(set1.union(set2))

combined_warehouse = warehouse1 | warehouse2

sorted_desc = dict(
    sorted(combined_warehouse.items(), key=lambda x: x[1][1], reverse=True)
)

print(sorted_desc)
