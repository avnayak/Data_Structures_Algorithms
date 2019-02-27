class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
            
        else:
            r=BinaryTree(newNode)
            r.rightChild=self.rightChild
            r=self.rightChild
    

    def getRightChild(self):
        return self.rightChild



    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

a=BinaryTree("Vijay")
a.insertLeft("Mummy")
a.insertLeft("k")
a.getRootVal()
