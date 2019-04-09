import sys
class Node(object):
     def __init__(self, x):
         self.key = x
         self.left = None
         self.right = None

        
# Insert Node
     def insert(self, data):

        if self.key!=None:
            if data < self.key:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.key:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
     def minDepth (self, root ) :
        if not root :
            return 0
        if not root.left and not root.right: # o n l y l e a v e s w i l l have 1
            return 1
        ans = sys.maxsize
        if root .left:
            ans = min ( ans , self.minDepth ( root.left) )
        if root.right :
            ans = min ( ans , self.minDepth(root.right) )
        return ans+1
        
root=Node(72)
root.insert(4)
root.insert(90)
root.insert(70)
root.insert(459)
root.insert(29)
print root.minDepth(root)
