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

#   List Functions

#_sum(Calculate the sum of elements of the list)

print(sum(lst))


#_Max(print largest value)

print(max(lst))


#_Min(print smallest value)

print(min(lst))


#_len(to calculate max elements)

print(len(lst))


#_append(adding an element at a time to list !!Can only add one element at a time!!)

lst.append(20)
print(lst)


#_insert(to insert an element at a specific index)

lst.insert(1, 'nadeem')
print(lst)


#_extend(To add elements from another list)
lst1 = ['Yunus', 'Anand', 'Christy']
lst.extend(lst1)
print(lst)


#_math(To remove an element from list!!Can only remove one element at a time!!)

lst.remove('nadeem')
print(lst)


#_pop(To remove the last element from a !!stack!!)

lst.pop()
print(lst)


#_reverse(To reverse the list)

# lst.reverse()
# print(lst)


#_sort(To sort the list in ascending order)

num = [5,43.32,3,5,2,4,788,]
stud = ['Nadeem','Yunus','Anand', 'Chridty']
num.sort()
stud.sort()
print(num)
print(stud)

#_sort in descending order

stud.sort(reverse=True)
print(stud)

#_To sort without changing list using sorted function

sorted_stud = sorted(stud)
print(sorted_stud)

#_To know the index number of a certain element
std = ['Nadeem','Yunus','Anand', 'Chridty']
print(std.index('Chridty'))

#_To check for an element is present in list

# print('Nadeem' in std)

#_To list the elements in line by line format

# for element in std:
#     print(element)