#creation of list
prog_lang=['c','c++','python','java','html','css','javascript','react js','angular','flutter']
print(prog_lang)
print(type(prog_lang))
print("-----------------------------------------------------------------------------------------------")
#iterating through list elements without index
for i in prog_lang:
    print(i)
print("-----------------------------------------------------------------------------------------------")
#iterating through list elements with index
for i in range(len(prog_lang)):
    print(prog_lang[i])