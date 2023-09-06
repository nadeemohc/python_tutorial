#LOOPS

#1 WHILE LOOP
#2 FOR LOOP

#
# #1 WHILE LOOP
#
#
# #SYNTAX
#
# #1 Initialization
# #2 Condition
# #3 increment or decrement
#
#
# #EXAMPLES
#
# #EX_1
#
# i = 1               #initialization
# while(i <= 10):     #condition
#     print("hello")  #statement
#     i += 1            #increment
#
#
# #EX_2
#
# i=1
# while(i <= 20):
#     print(i)
#     i += 1
#
#
# #EX_3
#
# i = 20
# while(i >= 1):
#     print(i)
#     i -= 1
#
# #EX_4
#
# x = int(input("enter a number"))
# i = 1
# while(i <= 10):
#     result = i * x
#     print(result)
#     i += 1
#
# # 1 FOR LOOP
#
# # SYNTAX
#
# # 1 Initialization
# # 2 Condition
# # 3 increment or decrement
#
# #EX_1
#
# for i in range(1,11):
#     print(i)
#     i+=1


# #EX_2
#
# for i in range(10):
#     print("hello")
#     i+=1



#EX-3

# for i in range(20,-1,(-1)):
#     print(i)


#
# #EX_4
#
# for i in range(1,31,2):
#     print(i)



#EX_5

# for i in range(10):     #0 to upper limit-1
#     print(i)
#


#EX_6_(program that prints numbers from 1 to 10)

# i = int(input("Enter the lower limit"))
# j = int(input("Enter the upper limit"))
# for x in range(i,j+1):
#     print(x)
#     x+=1



#EX_7_(program that prints all the even numbers from 1 to 20.)
# i = int(input("Enter the lower limit"))
# j = int(input("Enter the upper limit"))
# for x in range(i,j+1,1):
#     if x % 2 == 0:
#         print(x)



#EX_8_(program that calculates and prints the sum of all the numbers from 1 to 10.)

# y = 0
# i = int(input("Enter the lower limit"))
# j = int(input("Enter the upper limit"))
# for x in range(i,j+1):
#     y+=x
# print(y)



#EX_9(program that takes an integer as input and prints its multiplication table from 1 to 10.)

# i = 1
# y = 10
# num = int(input("Enter the number"))
# for x in range(i,y+1):
#     mul = num * i
#     print(mul)
#     i += 1



#EX_10( program that prints the following pattern using nested loops)


