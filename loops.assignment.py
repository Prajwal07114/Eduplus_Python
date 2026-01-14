
# WHILE LOOP PROGRAMS

# 1. Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Print even numbers between 1 and 50
j=2
while j<=50:
    print(j)
    j+=2

# 3. Sum of first 20 natural numbers
j=1
sum=0
while j<=20:
    sum+=j
    j+=1
print("Sum of first 20 natural numbers:",sum)

# 4. Multiplication table of 7
i = 1
while i <= 10:
    print(f"7 x {i} : {7*i}")
    i += 1

# 5. Reverse a number
num = int(input("Enter number to reverse: "))
rev=0
while num!=0:
    rev=rev*10+num%10
    num=num//10
print(rev)
# 6. Count digits
temp = int(input("Enter  number: "))
num=temp
count=0
while num>0:
    count+=1
    num//=10
print("Number of digits:", count)

# 7. Factorial
num = int(input("Enter number : "))
facto = 1
while num > 0:
    facto *= num
    num -= 1
print("Factorial:", facto)

# 8. Fibonacci up to 50
p,q = 0, 1
while p <= 50:
    print(p, end=" ")
    temp = p+q
    p=q
    q=temp


# 9. Palindrome check
num = int(input("Enter number for palindrome check: "))
temp = num
rev=0
while num !=0:
    rev = rev*10+num%10
    num//=10
if temp == rev:
    print("palindrome")
else:
    print("not palindrome")

# 10. Input until exit
while True:
    val = input("Enter value (type 'exit' to stop): ")
    if val.lower() == "exit":
        break



# DO-WHILE LOOP 

# 1. Print 1 to 10
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

# 2. Take input until positive number
while True:
    num = int(input("Enter positive number: "))
    if num > 0:
        break

# 3. Menu until Quit
while True:
    print("\n1. Add\n2. Subtract\n3. Quit")
    choice = input("Enter choice: ")
    if choice == "3":
        break

# 4. Table of 19
i = 1
while True:
    print(f"19 x {i} = {19*i}")
    i += 1
    if i > 10:
        break

# 5. Password check
while True:
    pwd = input("Enter password: ")
    if pwd == "admin":
        print("Access Granted")
        break

# 6. Sum of digits
num = int(input("Enter number: "))
total = 0
while True:
    total += num % 10
    num //= 10
    if num == 0:
        break
print("Sum of digits:", total)

# 7. Print 10 to 1
i = 10
while True:
    print(i)
    i -= 1
    if i == 0:
        break

# 8. Prime check
num = int(input("Enter number to check prime: "))
i = 2
is_prime = True
while True:
    if i >= num:
        break
    if num % i == 0:
        is_prime = False
        break
    i += 1
print("Prime" if is_prime else "Not Prime")

# 9. Odd numbers 1 to 30
i = 1
while True:
    print(i)
    i += 2
    if i > 30:
        break

# 10. Product until 0
product = 1
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    product *= num
print("Product:", product)


# 1. Print 1 to 20
for i in range(1,21):
    print(i)

# 2. Write a for loop to print the square of numbers from 1 to 10.
for i in range(1,11):
    print(i*i)

#Use for loop to display even numbers from 2 to 40.

for i in range(2,41):
    if i%2==0:
     print(i)

# 4. Write a for loop to print the multiplication table of 12.
for i in range(1,11):
    print(i*12)

# 5. Create a for loop to calculate factorial of a given number.
num = int(input("Enter your num : "))

fact=1
for i in range(1,num+1):
    fact *=i
    print(num,fact)

# 6. Write a for loop to print elements of a list containing 10 integers.
helo=[]
for i in range(1,11):
    helo.append(i)
for item in helo:
        print(item)

# 7. Write a for loop to count how many vowels are in a given string.

given_string = input("Enter string")

count=0
for vowel in given_string:
     
     if vowel in 'aeiouAEIOU':
        count+=1
print("total vowels : ",count)

# 8. Use nested for loop to print a right-angled triangle pattern of stars (*).
rows = int(input("enter rows : "))
for i in range(1,rows+1):
    for j in range(0,i):
        print("*",end=" ")
    print()        





# 10. Write a for loop to display only odd numbers from 1 to 25 and calculate their sum.
sum = 0
for i in range(1,26):
    if (i%2!=0):
     print(i)
     sum+=i
print(sum)