n=int(input("Enter the number of the customer to enter"))
dict_cus={}
for i in range (n):
    name=input("Enter the customer name : ")
    movies_list=input("Enter the list of movies where seperated by ,").split(',')
    movies_list=tuple(movies_list)
    dict_cus[name]=movies_list
print(dict_cus)


#Display all unique movies in the database.
set1=set()
for key,value in dict_cus.items():
    set1.update(value)

print(f"The total number of Unique movies watched by all customers are: {len(set1)}: {set1}")