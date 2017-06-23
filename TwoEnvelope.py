# -*- coding: utf-8 -*-
"""
Created on Fri May 26 10:29:56 2017
@author: Andrew

TWO ENVELOPE GAME
VERSION: E1 values even distribution $1 to $100, PLAY ALL VALUES

1. generate random number from 1 to 100 call it dollar value D
2. random distribute D, 2*D and D/2 into the four possible ordered pairs
   (D, 2D), (D, D/2), (2D, D) and (D/2, D) of 
   (E1,E2) such that we don't know if E1 or E2 
   is the original, doubled or halved value 
3. select E1, depending on pivotVAL, asign to STAY or SWITCH 

"""
import random as rand 

# select a dollar value 'D' between A and B 
A = 1
B = 100
nTrials = int(1E+4) ## set number trials to any integer, here 10000 
pivotVAL = 100 # set amount above which stay or swap 
HighSTAY = []
HighSWITCH = []

for trial in range(nTrials):
    
    # 1. random select D value 
    # 2. random asign to E1 or E2
    # 3. random halve or double D and asign to other E_ variable
    D = rand.randint(A,B) # D = random integer between A and B
    randomN = rand.randint(1,4) 
    if randomN == 1:
        E1 = D      # envelop 1 has the first selection
        E2 = D/2    # envelop 2 has the half first selection
    elif randomN == 2:
        E1 = D      # envelop 1 has the first selection
        E2 = 2*D    # envelop 2 has the double first selection
    elif randomN == 3:
        E1 = D/2    # envelop 1 has the half first selection
        E2 = D      # envelop 2 has the first selection
    else:
        E1 = 2*D    # envelop 1 has the double first selection
        E2 = D      # envelop 2 has the first selection
    
    if E1 > pivotVAL:
        HighSTAY.append(E1)
        HighSWITCH.append(E2)
    else:
        HighSTAY.append(E2)
        HighSWITCH.append(E1)

print("\nStay for greater than $", pivotVAL, ": av win $", '%.2f , ' \
      %(sum(HighSTAY)/nTrials), sep='')

print("Swap for greater than $", pivotVAL, ": av win $", '%.2f , ' \
      %(sum(HighSWITCH)/nTrials), sep='')

# TRYING TO WORK OUT THE SAMPLE SPACE
#A = []
#for a in range(1,101):
#    A.append(a) 
#    A.append(2*a)
#    A.append(a)
#    A.append(a/2)
#A.sort() 
#print(A)
#sum(A[0:225])
#sum(A[225:350])
#sum(A[350:400]) 
#
## WHY BETTER TO SWAP WITH ODD VALUES UNDER 50 
#ODD=0
#EVEN=0
#HALF=0
#for a in A[0:225]: 
#    if int(a) == a and a %2 == 1:
#        ODD += 1
#    elif int(a) == a and a %2 == 0:
#        EVEN += 1
#    else:
#        HALF += 1
    