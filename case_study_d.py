'''Case Study D: Customer Purchase Insights (E-commerce Scenario)
Scenario:
An e-commerce website tracks customer purchases daily. The company wants to derive insights about purchasing patterns.
Problem Statement:
Create a Python program where the user inputs daily customer purchase details as tuples — each containing (Customer Name, List of Products Purchased). Perform:
1.	Display the total number of unique products bought by all customers combined.
2.	Find customers who purchased both ‘Laptop’ and ‘Headphones’.
3.	Identify and display the most frequently purchased product(s) among all customers.'''



no_of_Customer = int(input("Enter the total no's : "))

cust_dict={}
for i in range(no_of_Customer):
  cust_name=input("Enter name of cust : ")
  objects=input("enter purchased items :  ").split(",")
  objects=tuple(objects)
  cust_dict[cust_name]=objects
  print (cust_dict)
#1

  unq=set()
  for k,v in cust_dict.items():
    unq.update(v)
    print(unq)

#2
Both=[]
for k,v in cust_dict.items():
 if "Laptop" and "Headphones" in v:
   Both.append(k)
   print(Both)
#3

frequent={}
for key,value in cust_dict.items():
    for i in value:
        if i not in frequent:
            frequent[i]=0
        frequent[i]+=1
print(frequent)


max=0
product=""
for key,value in frequent.items():
    if int(max) < value:
        max=value
        product=key
print(f"the most sales item is :{product} ")