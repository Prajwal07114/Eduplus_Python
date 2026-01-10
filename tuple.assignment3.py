#que1
import os
fruits=("mango","orange","grapes","strawberry","banana")
print(fruits)

#q2
mix_tup=("prajwal",7,7.9,True)
print(mix_tup[0])
print(mix_tup[1])
print(mix_tup[2])
print(mix_tup[3])

#Q3
nested_tup=(("India","Usa","Japan"),("Mah","Calafornia","Tokyo"))
print(nested_tup)

#q-4
print(fruits[-1])

#q-5
print(fruits[0:3])

#q-6
students=("prajwal","priya","durgesh")
print(len(students))

#q7

marks=(17,30,7,4,59,69)
print(max(marks))
print(min(marks))

#q8
print(sum(marks))

#q9
print(sorted(marks))

#q10
print(sorted(marks,reverse=True))

#q11
print(marks.count())

#q12
print(marks.index(7))

#q13
print("Python" in marks)

#q14
print("C++" not in marks)

#q15
num=tuple(range(0,10))
print(num)
#q16
boolean=(1,0,1,0,0,0,1)
print(any(boolean))

#q17
print(all(boolean))

#q18
first_name="prajwal"
last_name="_barsagade"

print(first_name + last_name)

#q19
mul=("AI","ML")
print(mul*3)

#20
names=("PRAJWAL","HARSHAL","DURGESH")
scores=(7,8,9)

viper=tuple(zip(names,scores))
print(viper)

#21
ag=(87,4,5,63,2)
print(tuple(reversed(ag)))
#22
alp=("HELLO")
print(min(alp))
print(max(alp))

#23
mod=("ads","ad")
a,b=mod
print(a)
print(b)

#24
modify=(1,2,6)
print(modify.append)

#25
li=[7,9,6,3,2]
tu=(7,1,4,3,30,0)


#26
summation=(1,2,3,4,5,6,7,8,9,10)
print(sum(summation))
print(len(summation))
#27
city=("mum","pune","ngp","delhi","hyd")
print(city[::-1])

#28
t=(1,5,3,8,6)
convert=list(t)
print(convert)
convert.append(7)
print(convert)
zy=tuple(convert)
print(zy)

#29
unpck=("prajwal",18,"DEV")
name,age,dept=unpck
print(name)
print(age)
print(dept)

#30
product_name=("apple","acer","HP")
price=(56000,78000,60000)
zipper=tuple(zip(product_name,price))
print(zipper)
print(sorted(zipper))