# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 08:30:37 2017
@author: Andrew

TWO ENVELOPE GAME: INITIAL ENVELOPE VALUES FROM 1 TO 100

Generates sample space of 400 envelope pairs and
each round a random selected pair's values are 
appended to appropriate STAY and SWAP lists

E1 values even distribution $1 to $100
E2 values 2*E1 or E1/2
Create global sample space of 400 ordered tuples, 
all possible combinations (E1,E2) and (E2,E1)  

"""
import random as rand 

N = 1E+4  #  <<------ SET NUMBER OF TRIALS HERE

nTrials = int(N) # make N interger not a 'float' 

Low = 1     
High = 100  

#___________GENERATE SAMPLE SPACE OF 400 ENVELOPES____________________  

#           [1~100, 1~100]                       E1 
chooseE1 =  [a for a in range(Low,High+1)] * 2 

#           [2 x E1] + [0.5 x E1]                E2
chooseE2 =  [2*a for a in range(Low,High+1)] + \
            [a/2 for a in range(Low,High+1)]

#   NOW CONCATENATE FOR EVERY POSSIBLE ORDERED TUPLE (E1,E2) & (E2,E1), 
#   THAT IS: 400 TUPLES (800 ENVELOPES)
T1 = chooseE1 + chooseE2  
T2 = chooseE2 + chooseE1 
SampleSpace = [(i,j) for (i,j) in zip(T1,T2)]           # 400 TUPLES

#  SELECT NTRIAL NUMBER OF TUPLES FROM THE PLAYSPACE, tuple[0]=STAY, tuple[1]=SWAP
AlwaysSTAY = []
AlwaysSWITCH = []
for trail in range(nTrials):
    Pair = rand.choice(SampleSpace) # ************ change to SampleSpace for original game
    AlwaysSTAY += [Pair[0]]
    AlwaysSWITCH += [Pair[1]]

# RESULTS FOR ALWAYS STAY AND ALWAYS SWAP 
print("\nAlways Switch      average win: $", '%0.2f ' \
      %(sum(AlwaysSWITCH)/len(AlwaysSWITCH)),sep='')
low = [i for i in AlwaysSWITCH if i <51] 
med = [i for i in AlwaysSWITCH if i >= 51 and i <= 100]
high = [i for i in AlwaysSWITCH if i > 100]
print("win values $0.50 to $50, ",' %.1f' \
      %(100*len(low)/nTrials),"%", sep='')
print("win values   $51 to $100, ", '%.1f' \
      %(100*len(med)/nTrials),"%",sep='')
print("win values  $102 to $200, ", '%.1f' \
      %(100*len(high)/nTrials),"%\n", sep='')

print("Always Stay        average win: $", '%.2f  ' \
      %(sum(AlwaysSTAY)/len(AlwaysSTAY)),sep='')
low = [i for i in AlwaysSTAY if i <51] 
med = [i for i in AlwaysSTAY if i >= 51 and i <= 100]
high = [i for i in AlwaysSTAY if i > 100]
print("win values $0.50 to $50, ",' %.1f' \
      %(100*len(low)/nTrials),"%", sep='')
print("win values   $51 to $100, ", '%.1f' \
      %(100*len(med)/nTrials),"%",sep='')
print("win values  $102 to $200, ", '%.1f' \
      %(100*len(high)/nTrials),"%\n", sep='')
# -----------------------------------------------------------------------------

#  OTHER STRATEGIES 
for pivotVAL in [11, 21, 41, 51, 61, 81, 101]: # [100, 101]: # 
    HighSTAY = []
    HighSWITCH = []
    
    for i,j in zip(AlwaysSTAY, AlwaysSWITCH):
        if i >= pivotVAL:
            HighSTAY.append(i)
            HighSWITCH.append(j)
        else:
            HighSTAY.append(j)
            HighSWITCH.append(i)
            
    print("Stay for greater than or equal: $", pivotVAL, ", av win $", '%.2f' \
          %(sum(HighSTAY)/nTrials), sep='')
    # SORT WIN VALUES INTO LOW MED HIGH BINS FOR STATS
    low = [i for i in HighSTAY if i <51] 
    med = [i for i in HighSTAY if i >= 51 and i <= 100]
    high = [i for i in HighSTAY if i > 100]
    print("win values $0.50 to $50, ",' %.1f' \
          %(100*len(low)/nTrials),"%", sep='')
    print("win values   $51 to $100, ", '%.1f' \
          %(100*len(med)/nTrials),"%",sep='')
    print("win values  $102 to $200, ", '%.1f' \
          %(100*len(high)/nTrials),"%", sep='')

    print("Swap for greater than or equal: $", pivotVAL,  ", av win $", '%.2f' \
          %(sum(HighSWITCH)/nTrials), sep='')
    # SORT WIN VALUES INTO LOW MED HIGH BINS FOR STATS
    low = [i for i in HighSWITCH if i <51] 
    med = [i for i in HighSWITCH if i >= 51 and i <= 100]
    high = [i for i in HighSWITCH if i > 100]
    print("win values $0.50 to $50, ",' %.1f' \
          %(100*len(low)/nTrials),"%", sep='')
    print("win values   $51 to $100, ", '%.1f' \
          %(100*len(med)/nTrials),"%",sep='')
    print("win values  $102 to $200, ", '%.1f' \
          %(100*len(high)/nTrials),"%\n", sep='')

#------------------------------------------------------------------------------

# calculate chance of switch increase over ntrials in model
for D_val in [0.5, 1, 2, 20, 21, 40, 41, 50, 51, 60, 61, 80, 81, 100, 102]: 
    # generates list of ONE D_val, 
    # one for each time it's switch val is greater
    D = [i for (i, j) in zip(AlwaysSTAY, AlwaysSWITCH) if i==D_val and j>i]

    # count the lenght of the list divided by number of vals in original 
    D_up = len(D)/AlwaysSTAY.count(D_val) 

    print("for $", '%.2f ' %D_val, "chance of Switch increase: ", '%.1f' \
          %(100*D_up), "%", sep='')
