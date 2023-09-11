#1. List

#how to define

# lst = []
#
# print(type(lst))

# ls = list()
# print(type(ls))

lst = [10,45,76,True,False]
lst[2]=67
# lst = [10,45.7,76,'Nadeem','Nadeem',45.7,True,False]
print(lst)
#   List supports hetrogenous data
#   Insertion order is preserved
#   Supports duplication
#   Its mutable(editable)

for i in lst:
    if i % 2 == 0:
        print(i)