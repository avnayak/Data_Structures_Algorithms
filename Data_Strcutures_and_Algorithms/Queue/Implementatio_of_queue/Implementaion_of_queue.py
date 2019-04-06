class queue(object):
    def __init__(self):
        self.items=[]        
    
    def isEmpty(self):
        return self.items==[]
        
    def firstIn(self,newElement):
        return self.items.insert(0,newElement)
        
    def firstOut(self):
        return self.items.pop()
        
x=queue()
print x.isEmpty()
print x.firstIn(45)
print x.firstIn(4)
print x.firstIn(0,78)
print x.firstOut()





