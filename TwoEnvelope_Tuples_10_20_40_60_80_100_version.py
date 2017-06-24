# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:41:37 2017
@author: Andrew 
TWO ENVELOPES, ATHK1001 tutorial version** 
(**only play when revealed value is 10, 20, 40, 60, 80 or 100)
E1 values even distribution $1 to $100
E2 values 2*E1 or E1/2
Create global sample space of 400 ordered tuples, 
all possible combinations of E1 and E2,  
from which the PlaySpace of 21 ordered tuples is selected
so to model the ATHK1001 tutorial version

"""
import random as rand 

N = 1E+3  #  <<------ SET NUMBER OF TRIALS HERE

nTrials = int(N) # make N interger not a 'float'

#___________GENERATE SAMPLE SPACE OF 400 ENVELOPES____________________  

#           [1~100, 1~100]                       E1 
chooseE1 =  [a for a in range(1,101)] * 2 

#           [2 x E1] + [0.5 x E1]                E2
chooseE2 =  [2*a for a in range(1,101)] + \
            [a/2 for a in range(1,101)]

#   NOW CONCATENATE FOR EVERY POSSIBLE ORDERED TUPLE (E1,E2) & (E2,E1), 
#   THAT IS: 400 TUPLES (800 ENVELOPES)
T1 = chooseE1 + chooseE2  
T2 = chooseE2 + chooseE1 
SampleSpace = [(i,j) for (i,j) in zip(T1,T2)]           # 400 TUPLES

#__________LIMIT THE PLAYSPACE TO ONLY TUPLES THAT START WITH PLAY VALUE_____ 

Play = [10,20,40,60,80,100] 
PlaySpace = [T for T in SampleSpace if T[0] in Play]    # 21 TUPLES 

#  SELECT NTRIAL NUMBER OF TUPLES FROM THE PLAYSPACE, tuple[0]=STAY, tuple[1]=SWAP
AlwaysSTAY = []
AlwaysSWITCH = []
for trail in range(nTrials):
    Pair = rand.choice(PlaySpace) # ************ change to SampleSpace for original game
    AlwaysSTAY += [Pair[0]]
    AlwaysSWITCH += [Pair[1]]

# RESULTS FOR ALWAYS STAY AND ALWAYS SWAP 
print("\nAlways Switch average win: $", '%0.2f ' \
      %(sum(AlwaysSWITCH)/len(AlwaysSWITCH)),sep='')
low = [i for i in AlwaysSWITCH if i <60] 
med = [i for i in AlwaysSWITCH if i >= 60 and i < 120]
high = [i for i in AlwaysSWITCH if i >= 120]
print("win values $5 to $50, ",' %.1f' \
      %(100*len(low)/nTrials),"%", sep='')
print("win values $60 to $100, ", '%.1f' \
      %(100*len(med)/nTrials),"%",sep='')
print("win values $120 to $200, ", '%.1f' \
      %(100*len(high)/nTrials),"%\n", sep='')

print("Always Stay average win: $", '%.2f  ' \
      %(sum(AlwaysSTAY)/len(AlwaysSTAY)),sep='')
low = [i for i in AlwaysSTAY if i <60] 
med = [i for i in AlwaysSTAY if i >= 60 and i < 120]
high = [i for i in AlwaysSTAY if i >= 120]
print("win values $5 to $50, ",' %.1f' \
      %(100*len(low)/nTrials),"%", sep='')
print("win values $60 to $100, ", '%.1f' \
      %(100*len(med)/nTrials),"%",sep='')
print("win values $120 to $200, ", '%.1f' \
      %(100*len(high)/nTrials),"%\n", sep='')
# -----------------------------------------------------------------------------

#  OTHER STRATEGIES 
for pivotVAL in [20,40,60,80,100]: # [51, 102]: # 
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
    low = [i for i in HighSTAY if i <60] 
    med = [i for i in HighSTAY if i >= 60 and i < 120]
    high = [i for i in HighSTAY if i >= 120]
    print("win values $5 to $50, ",' %.1f' \
          %(100*len(low)/nTrials),"%", sep='')
    print("win values $60 to $100, ", '%.1f' \
          %(100*len(med)/nTrials),"%",sep='')
    print("win values $120 to $200, ", '%.1f' \
          %(100*len(high)/nTrials),"%", sep='')

    print("Swap for greater than or equal: $", pivotVAL,  ", av win $", '%.2f' \
          %(sum(HighSWITCH)/nTrials), sep='')
    # SORT WIN VALUES INTO LOW MED HIGH BINS FOR STATS
    low = [i for i in HighSWITCH if i <60] 
    med = [i for i in HighSWITCH if i >= 60 and i < 120]
    high = [i for i in HighSWITCH if i >= 120]
    print("win values $5 to $50, ",' %.1f' \
          %(100*len(low)/nTrials),"%", sep='')
    print("win values $60 to $100, ", '%.1f' \
          %(100*len(med)/nTrials),"%",sep='')
    print("win values $120 to $200, ", '%.1f' \
          %(100*len(high)/nTrials),"%\n", sep='')

#------------------------------------------------------------------------------

# calculate chance of switch increase over ntrials in model
print("chance of switch increase from last trial:")
for D_val in Play: 
    # generates list of ONE D_val, 
    # one for each time it's switch val is greater
    D = [i for (i, j) in zip(AlwaysSTAY, AlwaysSWITCH) if i==D_val and j>i]
    
    # count the lenght of the list divided by number of vals in original 
    D_up = len(D)/AlwaysSTAY.count(D_val) 
    
    print("for $", '%.2f ' %D_val, "chance of Switch increase: ", '%.1f' \
          %(100*D_up), "%", sep='')



# D values over exact sample space


    
    
#     ******** ANALYSIS OVER EXACT SAMPLE SPACE *********    
# chance of switch increase over the exact sample space 
#print("\nAnalytical chance of switch increase over perfect sample space:")
#P1=[10,10,10,10,20,20,20,20,40,40,40,40,60,60,60,80,80,80,100,100,100]
#P2=[ 5, 5,20,20,10,40,10,40,20,80,20,80,30,120,30,40,40,160,50, 50,200]
#
#for D_val in Play: 
#    D = [i for (i, j) in zip(P1, P2) if i==D_val and j>i]
#    D_up = len(D)/P1.count(D_val) 
#    print("for $", '%.2f ' %D_val, "chance of Switch increase: ", '%.1f' \
#          %(100*D_up), "%", sep='')  
#
#A = P1 + P2
#A.sort()
#L=len(A)
#print("\n1st quartile",A[int(L*0.25)])
#print("2nd quartile",A[int(L*0.5)])
#print("3rd quartile",A[int(L*0.75)])
#print("Top decile",A[int(L*0.9)])