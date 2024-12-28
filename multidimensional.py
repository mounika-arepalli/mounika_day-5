#multidimensional lists-list inside a list
list=[[1,2,3],[4,5,6],[7,8,9]]
print(list,type(list))
print(list[0][0])
print(list[0][1])
print(list[0][2])
print(list[1])
print(list[2])
print("----------------------------------------")
list=[[[1,2,3],[4,5,6],[7,8,9,'hi']]]
print(list,type(list))
print(list[0][2][3])