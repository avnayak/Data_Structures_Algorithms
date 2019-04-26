# Definition for a binary tree node.
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
#class Solution(object):
     def isBalanced(self,root):
            def buildTree(self,root):
                if root is None:
                    return False
                lh=buildTree(root.left)
                rh=buildTree(root.right)
                v=lh-rh
                if lh ==-2 or rh==-2 or abs(v)>1:
                    return -2
                return max( lh , rh )+1
	    return True
root=Node(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)

print root.isBalanced(root)
