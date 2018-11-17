# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:02:37 2018

@author: dell
"""

#   >>> RiskGame([1,2,6], [1, 5])
#    'Defender loses 2 armies.'
#    >>> RiskGame([6,2,6], [6, 6])
#    'Attacker loses 2 armies.'
#    >>> RiskGame([1,4,1], [1, 2])
#    'Attacker loses 1 army and defender loses 1 army.'

def RiskGame(attacker, defender): 
    attacker.reverse()
    defender.reverse()
    a=0
    b=0

    for i in range(2):
        if attacker[i]>defender[i]:
            a=a+1
        else:
            b=b+1
    if a==0:
        print ('',end='')
    if a==1:
        print ('Attacker loses 1 army.',end='')
    if a==2:
        print ('Attacker loses 2 armies.',end='')
    if b==0:
        print ('')
    if b==1:
        print ('Attacker loses 1 army.',end='')
    if b==2:
        print ('Attacker loses 2 armies.',end='')
    print ('')
    return a,b    

w=RiskGame([1,4,1], [1, 2])

print (w) 

#print (w[0])
#print (w[1])