def printTwos(n):
    
    
    if n==1:
        return str(1)
#    if n==2:
#        return '2'+' * ' +'1'
    if n>2 and n%2!=0:		
        return str(int(n))
        
    else:
        b=(printTwos(n/2)).count('2')
        if b%2==0 :
            
            return '2'+' * '+ (printTwos(n/2))
        if b%2!=0:
            return (printTwos(n/2))+' * '+'2'
n=32
a=printTwos(n)
print (a)