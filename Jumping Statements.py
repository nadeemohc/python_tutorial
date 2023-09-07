#JUMPING STATEMENTS


#1 BREAK
#2 CONTINUE
#3 PASS


#Syntax

#BREAK

for i in range(1,51):
    if(i == 5):
        break               #stops the code if condition satisfies
    print(i)
    i+=1
    continue


#CONTINUE

for i in range(1,50):
    if(i == 45):
        continue            #Skips the loop when condition satisfies
    print(i)
    i+=1


#PASS

for i in range(1,50):
    if(i == 25):
        pass                #No change in code (does Nothing)
    print(i)
    i+=1