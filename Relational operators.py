#RELATIONAL OPERATORS

#COMPARISON

#<,>,<=,>=,==,!=

#True / False


#EX_1
if (10>20):
    print(10, "greater")
else:
    print(20, "greater")


#LOGICAL OPERATORS

#1 AND(&)
#2 OR(|)
#3 NOT(!)
#4 XOR(^)


#AND

#   A  B   Y = A*B
#   1  0     0
#   0  0     0
#   1  1     1
#   0  1     0

#OR

#   A  B   Y = A^B
#   1  0     1
#   0  0     0
#   1  1     0
#   0  1     1

#NOT

#   A   Y = A!B
#   1     0
#   0     1

#XOR

#   A  B   Y = AB
#   1  0     1
#   0  0     0
#   1  1     1
#   0  1     1

#COMPOUND ASSIGNMENT OPERATORS

#EX_1
num=10
num+=1
print(num)


#EX_2
num1 = 10
num1-=1
print(num1)


#EX_3
x = 20
y = 10
sum = x + y
sum+=30
print(sum)