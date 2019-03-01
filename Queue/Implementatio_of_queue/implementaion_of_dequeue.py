    def addRear(self,newElement):
        return self.items.insert(0,newElement)
        
    def addFront(self,newElement):
        return self.items.append(newElement)
    
    def removeFront(self):
        return self.items.pop()
    
        
    def removeRear(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
x=queue()
print x.isEmpty()
print x.addRear(45)
print x.addRear(4)
print x.addFront(8)
print x.addFront(67)
print x.removeRear()
print x.removeFront()
