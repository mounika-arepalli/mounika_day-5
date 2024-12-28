num="123456"
#conversion of str to list
list_num=list(num)
print(num)
print(list_num)
res=''
for i in list_num:
    res=i+res
print(res)
