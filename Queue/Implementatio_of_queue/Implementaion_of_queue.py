class queue(object):
    def __init__(self):
        self.items=[]        
    
    def isEmpty(self):
        return self.items==[]
        
    def firstIn(self,position,newElement):
        return self.items.insert(position,newElement)
        
    def firstOut(self):
        return self.items.pop(0)
        
x=queue()
print x.isEmpty()
print x.firstIn(1,45)
print x.firstIn(2,4)
print x.firstIn(0,78)
print x.firstOut()





