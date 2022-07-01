import random
import time


print("***********LET'S START************")
pranjal=[int(input("Pranjal please enter the number {}".format(i))) for i in range(1,3)]
print()

bhumika=[int(input("Bhumika please enter the number {}".format(i))) for i in range(1,3)]
print()

print("pranjal's choice is======================> ",pranjal)
print("bhumika's choice is======================> ",bhumika)

winner=[random.randint(1,10) for j in range (1,5)]

print("************************************************************************")
print("\n*********************WINNING NUMBERS**********************************")

for k in winner:
    time.sleep(1.5)
    print(k,"\t \t \t",end="")     #/t is for space between the numbers


pranjal_p=0
bhumika_b=0

for p in pranjal:
    if p in winner:
          pranjal_p+=1

for b in bhumika:
    if b in winner:
          bhumika_b+=1

print("\n--------------------------RESULT----------------------------------------")

if pranjal_p>bhumika_b:
    for p1 in "PRANJAL IS WINNER":
             print(p1,end="")
             time.sleep(1)

elif bhumika_b>pranjal_p:
    for b1 in "BHUMIKA IS WINNER":
            print(b1,end="")
            time.sleep(1)

else:
    for x in "MATCH DRAW":
        print(x,end="")
        time.sleep(1)


print("\n**********************************THANKYOU********************************")












