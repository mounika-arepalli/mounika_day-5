#write a python program to read the size of list as input from the user & take the elements as input into the list & print it?
size=int(input("enter the size of the list:"))
list=[]
for i in range(size):
    list.append(input("enter the element:"))
print("user entered list is:",list)
