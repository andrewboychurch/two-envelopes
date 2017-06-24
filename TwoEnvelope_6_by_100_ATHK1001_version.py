# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:55:13 2017
@author: Andrew

Created on Wed May 31 08:41:37 2017
@author: Andrew 

    TWO ENVELOPES, ATHK1001 tutorial version** 
        (**only play when revealed value is 10, 20, 40, 60, 80 or 100)
    AND ***only play equal rounds of each value    
    E1 values even distribution $1 to $100
    E2 values 2*E1 or E1/2
    Create global sample space of 400 ordered tuples, 
    all possible combinations of E1 and E2: 
        (E1, 2*E1), (E1, E1/2), (2*E1, E1), (E1/2, E1) 
    from which the PlaySpace of 21 ordered tuples is selected
    so to model the ATHK1001 tutorial version

"""
import random as rand 

N = 6E+2 #  <<------ SET NUMBER OF TRIALS (default 600, that is 100 x 6)

nTrials = int(N) # make N interger not a 'float'

rounds = int(nTrials/6) # to better model tutorial version 6 values per round


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

#__________LIMIT THE PLAYSPACE TO ONLY TUPLES THAT START WITH PLAY VALUE_______ 
Play = [10,20,40,60,80,100] 
PlaySpace = [T for T in SampleSpace if T[0] in Play]    # 21 TUPLES 

#__________TO PLAY EACH VALUE EQUALLY USE INDIVIDUAL PLAYSPACES________________
PlaySpace10 = [T for T in PlaySpace if T[0] == 10]      # 4 TUPLES
PlaySpace20 = [T for T in PlaySpace if T[0] == 20]      # 4 TUPLES
PlaySpace40 = [T for T in PlaySpace if T[0] == 40]      # 4 TUPLES
PlaySpace60 = [T for T in PlaySpace if T[0] == 60]      # 3 TUPLES
PlaySpace80 = [T for T in PlaySpace if T[0] == 80]      # 3 TUPLES
PlaySpace100 = [T for T in PlaySpace if T[0] == 100]    # 3 TUPLES

#  GENERATE STAY AND SWAP LISTS OF NTRIALS/6 ROUNDS at each of SIX VALUES
AlwaysSTAY = []
AlwaysSWITCH = []
count = 0

while count < rounds:

        Pair = rand.choice(PlaySpace10)
        if Pair[0] == 10:
            AlwaysSTAY += [Pair[0]]
            AlwaysSWITCH += [Pair[1]]

        Pair = rand.choice(PlaySpace20)
        if Pair[0] == 20:
            AlwaysSTAY += [Pair[0]]
            AlwaysSWITCH += [Pair[1]]

        Pair = rand.choice(PlaySpace40)
        if Pair[0] == 40:
            AlwaysSTAY += [Pair[0]]
            AlwaysSWITCH += [Pair[1]]

        Pair = rand.choice(PlaySpace60)
        if Pair[0] == 60:
            AlwaysSTAY += [Pair[0]]
            AlwaysSWITCH += [Pair[1]]

        Pair = rand.choice(PlaySpace80)
        if Pair[0] == 80:
            AlwaysSTAY += [Pair[0]]
            AlwaysSWITCH += [Pair[1]]

        Pair = rand.choice(PlaySpace100)
        if Pair[0] == 100:
            AlwaysSTAY += [Pair[0]]
            AlwaysSWITCH += [Pair[1]]

        count +=1

#------------------------------------------------------------------------------
#   NTRIALS/6 ROUNDS FOR EACH STRATEGY OF STAY AT OR ABOVE PIVOT VALUE    
for pivotVAL in [20,40,60,80,100]:
    HighSTAY = []
    HighSWITCH = []
    
    for i,j in zip(AlwaysSTAY, AlwaysSWITCH):
        if i >= pivotVAL:
            HighSTAY.append(i)
            HighSWITCH.append(j)
        else:
            HighSTAY.append(j)
            HighSWITCH.append(i)

    #--------------------------------------------------------------------------
            
    print("\nSTAY for equal or greater than $", pivotVAL, ": $", '%.2f' \
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

    #--------------------------------------------------------------------------

    print("SWAP for equal or greater than $", pivotVAL,  ": $", '%.2f' \
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
          %(100*len(high)/nTrials),"%", sep='')

#------------------------------------------------------------------------------
# ALWAYS STAY STRATEGY 
print("\n\nSTAY ALWAYS average win:          $", '%.2f  ' \
      %(sum(AlwaysSTAY)/len(AlwaysSTAY)),sep='')
low = [i for i in AlwaysSTAY if i <60] 
med = [i for i in AlwaysSTAY if i >= 60 and i < 120]
high = [i for i in AlwaysSTAY if i >= 120]
print("win values $5 to $50, ",' %.1f' \
      %(100*len(low)/nTrials),"%", sep='')
print("win values $60 to $100, ", '%.1f' \
      %(100*len(med)/nTrials),"%",sep='')
print("win values $120 to $200, ", '%.1f' \
      %(100*len(high)/nTrials),"%", sep='')

#  ALWAYS SWITCH STRATEGY
print("\nSWAP ALWAYS average win:          $", '%0.2f ' \
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
#------------------------------------------------------------------------------
# calculate chance of switch increase over ntrials in model
#print("chance of switch increase from last trial:")
for D_val in Play: 
    # generates list of ONE D_val, 
    # one for each time it's switch val is greater
    D = [i for (i, j) in zip(AlwaysSTAY, AlwaysSWITCH) if i==D_val and j>i]
    
    # count the lenght of the list divided by number of vals in original 
    D_up = len(D)/AlwaysSTAY.count(D_val) 
    
    print("for $", '%.2f ' %D_val, "chance of Switch increase: ", '%.1f' \
          %(100*D_up), "%", sep='')



    
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
##
## D values over exact sample space
#print("\nD values $5 to $50, ",' %.1f' %(100*A.index(60)/L),"%", sep='')
#print("D values $60 to $100, ", '%.1f' %(100*(A.index(120)-A.index(60))/L),"%",sep='')
#print("D values $120 to $200, ", '%.1f' %(100*(L-A.index(120))/L),"%", sep='')
#

    
