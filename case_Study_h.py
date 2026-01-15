#Problem Statement:Write a Python program to take inputs as (Participant_Name, [List_of_Sports]) and perform:

sports = {}

no = int(input("Participant no : "))

for i in range(no):
  Participant_Name = ""
  List_of_Sports = []
  Participant_Name=input("Enter Participant Name : ")
  List_of_Sports = input("Enter Sports : ").split(',')
  
  sports[Participant_Name]=List_of_Sports

print(sports)

#1.	Display participants who are taking part in both ‘Cricket’ and ‘Football’.
helo=[]
for key,value in sports.items():
 if "Cricket" and "Football"  in value:
  helo.append(key)
  print(helo)

#2.	Find the total number of unique sports being played.


set1=set()
for key,value in sports.items():
  set1.update(value)
print(set1)

#3.	Create a tuple containing sports with the highest participation count.


