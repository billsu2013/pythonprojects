# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 20:32:24 2018

@author: dell
"""
#
#    >>> tictactoe([('X', ' ', 'O'), 
#                   (' ', 'O', 'O'), 
#                   ('X', 'X', 'X') ])
#    "'X' wins (horizontal)."
#    >>> tictactoe([('X', 'O', 'X'), 
#    ...            ('O', 'X', 'O'), 
#    ...            ('O', 'X', 'O') ])
#    'Draw.'
#    >>> tictactoe([('X', 'O', 'O'), 
#    ...            ('X', 'O', ' '), 
#    ...            ('O', 'X', ' ') ])
#    "'O' wins (diagonal)."
#    >>> tictactoe([('X', 'O', 'X'), 
#    ...            ('O', 'O', 'X'), 
#    ...            ('O', 'X', 'X') ])
#    "'X' wins (vertical)."

#def tictactoe(moves):
#
#    a=0
#     
#    for i in range(3):
#        if moves[i][1]==moves[i][2]==moves[i][0] :
#             return ("'%s' wins (horizontal)"%moves[i][1] )
#             a=1
#    for j in range(3):
#            if moves[1][j]==moves[2][j]==moves[0][j]:
#                return ("'%s' wins (vertical)."%moves[1][j] )
#                a=1
#    
#    if moves[0][0]==moves[1][1]==moves[2][2] or moves[0][2]==moves[1][1]==moves[2][0] :
#        return ("'%s' wins (diagonal)."%moves[1][1])
#        a=1
#    if a==0:
#         return ('Draw.')
#     
#tic=tictactoe([('X', 'O', 'O'), 
#    ('X', 'O', ' '), 
#    ('O', 'X', ' ') ])
#print (tic)
#


def tictactoe(moves):

    num=len(moves)
    a=False
    w=0
    for i in range(num):
        w=0
        for j in range(num):
            if moves[i][j]!=moves[i][0]:
               break
            if moves[i][j]==moves[i][0]:
               w=w+1
               if w==num:
                  return ("'%s' wins (horizontal)"%moves[i][0] )
                  a=True
                 
    for j in range(num):
            w=0
            for i in range(num):
                if moves[i][j]!=moves[0][j]:
                    break
                if moves[i][j]==moves[0][j]:
                    w=w+1
                    if w==num:
                        return ("'%s' wins (vertical)."%moves[0][j] )
                        a=True
                    
    w=0
    for i in range(num):
        for j in range(num):
            if i==j:
                if moves[i][j]!=moves[0][0]:
                    break                
                if moves[i][j]==moves[0][0]:
                    w=w+1
                    if w==num:
                       return ("'%s' wins (diagonal)."%moves[0][0])
                       a=True
    w=0
    for i in range(num):
        for j in range(num):                    
            if i+j==num-1:
                if moves[i][j]!=moves[num-1][0]:
                    break                
                if moves[i][j]==moves[num-1][0]:
                    w=w+1
                    if w==num:
                       return ("'%s' wins (diagonal)."%moves[num-1][0])
                       a=True
                    
    if a==False:
         return ('Draw.')
     
tic= tictactoe([('X', 'O', 'O'), 
('X', 'O', ' '), 
('O', 'X', ' ') ])
print (tic)

         