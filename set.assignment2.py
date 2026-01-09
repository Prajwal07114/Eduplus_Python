#que-1
countries = {"INDIA","RUSSIA","ARGENTINA","JAPAN","GERMANY"}
print(countries)

#que-2
NUM={1,3,7,6,5,7,3}
print(NUM)

#que-3
fruits=["mango","apple","orange","cherry","cotton_candy"]
fc=set(fruits)
print(fc)

#que-4
fc.add("banana")
print(fc)

#que-5
fc.update(["Prajwal","SD"])
print(fc)

#que-6
fc.add("SD")
print(fc)

#que-7
fc.remove("orange")
print(fc)

#q8
fc.discard(100)
print(fc)

#q9
fc.pop()
print(fc)

#q-10
fc.clear()
print(fc)

#q-11
A={1,2,3,4,5}
B={3,4,5,6,7,8}
print(A|B)
#q-12
print(A&B)
#q-13
print(A-B)
#q-14
print(A^B)

#q-15
print(A.issubset(B))

#q-16
print(B.issuperset(A))

#q-17
print(A.isdisjoint(B))

#q-18
print(4 in A)

#q-19
print(7 not in A)

#q-20
print(len(A))
#q-21
print(min(A))

print(max(A))

#q-22
print(sum(A))

#q-23
print(sorted(A))

#q-24
print(sorted(A,reverse=True))

#que-25
Boolean={0,1,0,1,1,0}
print(any(Boolean))

#que-26
print(all(Boolean))

#que-27
HELLO=Boolean.copy()
print(HELLO)

#que-28
del B
print(B)

#que-29
lop=[2,3,4,5,6,4]
gc=set(lop)
print(gc)

#que-30

class1 = {"prajwal","harshal","durgesh","ruturaj","yash"}

class2={"prajwal","yash","speed","drake","emiway","krsna"}

print(class1&class2)

print(class1-class2)

print(class1|class2)