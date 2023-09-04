#FLOW CONTROLS

#   There's 3 types of flow control statements:-
    #1 DECESION MAKING    (if, if__else, if__elif__else)
    #2 LOOPING            (for, while)
    #3 JUMPING            (break, continue, pass)



#1 DECISION MAKING

#SYNTAX

#if__else()

if(condition):
    print("statement")
else:
    print("statement")


#EX_1

age = int(input("enter your age: "))
if(age >= 18):
    print("Eligible to vote")
else:
    print("Not Eligible to vote")


#EX_2

num = int(input("Enter the number: "))
if(num >= 0):
    print("Entered Number is positive")
else:
    print("Entered number is negative")



#EX_3

num = int(input("Enter a number: "))
if(num % 2 == 0):
    print("Entered number is positive")
else:
    print("Entered number is negative")



#if__elif__else()

#SYNTAX

if(condition):
    print("Stmt")
elif(condition):
    print("stmt")
elif (condition):
    print("stmt")
elif(condition):
    print("stmt")
elif(condition):
    print("stmt")
else:
    print("statement")


#EX_1 (

num = int(input("Enter a Number"))
if(num < 0):
    print("Entered number is Negative")
elif(num > 0):
    print("Entered number is Positive")
else:
    print("Entered number is Zero")


#EX_2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if(num1 > num2):
    print("First Number is largest")
elif(num2 > num1):
    print("Second Numbeer is largest")
else:
    print("Entered Numbers are Equal")


#EX_3

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if(num1 > num2) & (num1 > num3):
    print("num1 is largest")
elif(num2 > num1) & (num2 > num3):
    print("num2 is largest")
else:
    print("num3 is largest")