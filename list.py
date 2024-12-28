#creation of list
#           0    1     2      3         4        5         6       7
prog_lang=['c','c++','java','python','flutter','cobaly','dart','javascript']
#           -8   -7     -6      -5       -4      -3       -2        -1
print(prog_lang)
print(type(prog_lang))
print("------------------------------------------------------------------------")
#accessing the list elements in both indexing 
print("accessing the list of elements by using positive indexing")
print(prog_lang[0])
print(prog_lang[1])
print(prog_lang[2])
print(prog_lang[3])
print(prog_lang[4])
print(prog_lang[5])
print(prog_lang[6])
print(prog_lang[7])
print("accessing the list of elements by using negative indexing")
print(prog_lang[-1])
print(prog_lang[-2])
print(prog_lang[-3])
print(prog_lang[-4])
print(prog_lang[-5])
print(prog_lang[-6])
print(prog_lang[-7])
print(prog_lang[-8])
#slicing
#extract a part of list or divide the list into sub lists
'''
:stop
start:stop
start:stop:str=epsize
'''
print("slicing of list:")
print(prog_lang[:4])
print(prog_lang[4:])
print(prog_lang[::2])