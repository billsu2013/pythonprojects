# -*- coding: utf-8 -*-
"""
Created on Tue May  1 21:52:11 2018

@author: dell
"""

# Create a function that appends the name and email to the end of a named file.
def addEmail(filename, name, email):
    f = open(filename, 'w') # replace the mode

    
    # Append name and email, each record should end with '\n'.
    
    f.write("%s %s\\n" % (name,email))
#    f.write(email)
    # close file
    f.close()
    return f # do not remove this line 


a=addEmail('emails.txt', 'Mary', 'mary@gmail.com')
#file=open(emails.txt,'r')
#print (file.readline())


#print (file)