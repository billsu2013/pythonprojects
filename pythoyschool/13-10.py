#records = []
#records.append({'x':1, 'y':2, 'z':3})
#records.append({'z':6, 'y':5, 'x':4})
#l=sorted(records[0].items(),key=lambda x:x[0],reverse=False) 
#print (l)
def gethostname(ip_address):
    import socket
    w=socket.gethostbyaddr(ip_address)
    
    return str(w[0])+str(w[2])

a=gethostname('127.0.0.1')
print (a)