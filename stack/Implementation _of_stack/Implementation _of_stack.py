class stack(object):
    def __init__(self):
        self.items=[]        
    
    def isEmpty(self):
        return self.items==[]
        
    def lastElement(self):
        return self.items.pop()
    
    def seeFirstElement(self):
        return self.items[len(self.items)-1]
    
    def add(self,newNumber):
        return self.items.append(newNumber)
        
x=stack()
print x.isEmpty()
print x.add(4)
print x.add(78)
print x.lastElement()
print x.seeFirstElement()



