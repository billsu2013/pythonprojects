# -*- coding: utf-8 -*-
"""
Created on Wed May  2 12:04:54 2018

@author: dell
"""

# The test score of the students in a class is stored in a file in the
# following format:
#
# Name    Score
# John    89
# Susan   85
#
# Write a function to read the scores and compute the average score of the
# class. (Ignore the first line which contains the field headers).

def getWinner(filename):
    # read file using readlines() 
    results = open(filename)         

    # initialize variables
    winner =[]
    
    max_score =0 

    # process results
    for line in results:
        tokens = line.split(',')    # split line using ',' separator   
        name =tokens[0]                   # get the name
        b=tokens[1].strip().split(' ') + tokens[2].strip().split(' ')
        print ("b is:"+ str(b))
        
        score_flatmap = map(float,b)
        print (list(score_flatmap))
        
        score = list(map(float,b))
        print (str(score))
        #score = list(map(float,tokens[1].split(' ')))
#        score2=list(map(float,tokens[2].split(' ')))# get scores
#        
#        score.append(score2)
        score.sort()
        print (str(score))
        
        # compute average, throwing the worst and best scores.
        #ave =(sum(score)-score[0]-score[-1])/len(score-2)   
        print (score[1:-1])         
        ave =(sum(score[1:(len(score)-1)]))/(len(score)-2)
        print (ave)
        if ave > max_score:
           winner =name              # save name of highest score so far
           max_score =ave           # save highest score

    return "%s [%.1f]" % (winner, max_score) 

a=getWinner('J:\pythonprojects\pythoyschool\grade.txt')
print (a)