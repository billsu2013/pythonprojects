# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def pairwiseScore(seqA, seqB): 
    
    Score = 0
    J=0
    print (seqA)
    for i in range(len(seqA)):
        
        if seqA[i]==seqB[i]:
           Score = Score+1
           J =J+1
           print ('|',end='')
           if i>=1 and seqA[i-1]==seqB[i-1]:
              if J%2==0:
                 Score = Score+3
                 J=0
                 
        if seqA[i]!=seqB[i]:
           Score=Score - 1
           print (' ',end='')
           J=0
    print('')
    print (seqB)       
    return  Score
    
w=pairwiseScore("GATAAATCTGGTCT", "CATTCATCATGCAA")

print (w)

