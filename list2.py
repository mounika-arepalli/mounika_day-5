#write a python program to print the count of null values present in the list?
list=['c','python','','','java','']
null_count=0
#condition to check number of null elements present in the list
for i in list:
    if(i==''):
        null_count+=1
print("number of null values are:",null_count)