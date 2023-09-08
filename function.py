#FUNCTIONS

#USES:-

#REUSABILITY
#TO REDUCE LENGTH OF PROGRAM



#SYNTAX
# def fn_name(arguments):
#     #fn_definition
#
# #call()


# We can create function in 3 methods:-

#   1 Function without argument and no return type
#   2 Function with arguments and no return type
#   3 Function with argument and return type


#   1 Function without argument and no return type


#   Adding two numbers

#

#   To perform addition multiple times you just needed to call the function multiple times.
#   Hence we can reduce the line of code.



#EX_1 (To greeet the user)
#
# def greet():
#     print("Hello, Nadeem")
#
# greet()
# greet()
# greet()
# greet()
#
# #EX_2 (function that prints any custom message of your choice)
#
# def message():
#     print("""Message:
#     Hello There,
#     How was your day?""")
# message()
#
# #EX_3 (function that prints numbers from 1 to 5)
#
# def numbers():
#     print("Numbers are: ")
#     for i in range(1,6,1):
#         print("\t\t\t",i)
# numbers()
#
#
# #EX_4 (function that prints your name when called)
#
# def say_my_name():
#     print("Heisenberg")
# say_my_name()
#
# #EX_5 (function that prints "Good morning!" when called)
#
# def greet():
#     print("Good Morning")
# greet()


#EX_6 (Calculator)

#FUNCTIONS_SECTION
# def addition():
#     num1 = int(input("Enter a Number: "))
#     num2 = int(input("Enter a Number: "))
#     sum: int = num1 + num2
#     print("Sum of entered numbers:",sum)
#
# def subtraction():
#     num1 = int(input("Enter the Number: "))
#     num2 = int(input("Enter the Number: "))
#     diff: int = num1 - num2
#     print("Difference of entered numbers:",diff)
#
# def multiplication():
#     num1 = int(input("Enter the Number: "))
#     num2 = int(input("Enter the Number: "))
#     mul = num1 * num2
#     print("Product of entered numbers:",mul)
#
# def division():
#     num1 = int(input("Enter the Number: "))
#     num2 = int(input("Enter the Number: "))
#     quotient: float = num1 / num2
#     print("Quotient of entered numbers: ",quotient)
#
# def modulus():
#     num1 = int(input("Enter the number: "))
#     num2 = int(input("Enter the number: "))
#     modulus: int = num1 % num2
#     print("Remainder of the entered numbers: ",modulus)
#
#
#
# print("Available operations in calculator:-\n"
#       "1. Addition\n"
#       "2. Subtraction\n"
#       "3. Multiplication\n"
#       "4. Quotient\n"
#       "5. Remainder\n")
# opr = int(input("Select an operation from below:"))
# if(opr == 1):
#     print(addition())
# elif(opr == 2):
#     print(subtraction())
# elif(opr == 3):
#     print(multiplication())
# elif(opr == 4):
#     print(division())
# elif(opr == 5):
#     print(modulus())
# else:
#     print("Invalid Entry")

#   2 Function with arguments and no return type

#Syntax

# def fn_name():
#     condition
# call()


#EX_1

# def add(num1 , num2):
#     sum = num1 + num2
#     print(sum)
#
# add(1,2)


#EX_2

# def Area_rect(l,b):
#     area = 2*(l+b)
#     print("Area of the rectangle is: ",area)
#     Area_rect(3,8)



#EX_3

def ar_crcl(r):
    area = (3.14*(r**2))
    print("Area of circle: ",area)


ar_crcl(7)