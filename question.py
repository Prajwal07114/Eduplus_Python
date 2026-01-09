#QUE1
list=[0,1,2,3,4,5,6,7,8,9]
print(list)
#QUE2
que_2=type([7,"prajwal",7.6,True])
print(que_2)

#QUE3
que_3=["hello","prajwal","hi",1,2,3,4,5,6,7]
print(que_3)
print(que_3[0])
MIDDLE=len(que_3)/2
print(MIDDLE)
print(que_3[5])

print(que_3[-1])

print(que_3[0:3])

print(que_3[-3:])

que_3[1]="college"
print(que_3)


que_3.append("welcome")
print(que_3)

que_3.insert(2,"gg")
print(que_3)

ext=["bye","bye"]
que_3.extend(ext)
print(que_3)

que_3.remove("hello")
print(que_3)

que_3.pop(3)
print(que_3)

del que_3[0]
print(que_3)

que_3.clear()
print(que_3)

new_list=["apple","mango","banana","orange","strawberry","cotton_candy"]
print(new_list)

print("apple" in new_list)
print(new_list)

new_list.index("apple")
print(new_list)

new_list.count("orange")
print(new_list)

new_list.sort()
print(new_list)

new_list.sort(reverse=True)
print(new_list)

new_list.reverse()
print(new_list)

hello=new_list.copy()
print(hello)

gg=new_list + hello
print(gg) 