#alist=[]
#def view():
#    print (alist)
#    
#def push(s):
#
#    alist.append(s)
#
#def pop():
#    del alist[-1]
#    
#    
##push()
#for i in range(10):
#    push(i)
#print (alist)
#
# 
#pop()
#print (alist)

# create a root

#class Node:
#    
#    def __init__(self,data):
#        self.right=None
#        self.left=None
#        self.data=data
#        
#    def PrintTree(self):
#        print(self.data)
#        
#root=Node(10)
#
#root.PrintTree()
        
#insert a node
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insert(self,data):
        if self.data:
        
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
                
    
                
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
            
    def PrintTree(self):
#        if self.left:
#            self.left.PrintTree()
        print(self.data)        
#        if self.right:
#            self.right.PrintTree()
    

root=Node(10)
root.insert(5)
root.insert(11)
root.insert(4)   
root.insert(15)

root.PrintTree()     