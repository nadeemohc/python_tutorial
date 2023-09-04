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