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
     def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q=[root]#List with the root value
        ans=[]
        i=0
        while q:
            temp=[]
            tempAns=[]
            direction='L'
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
     def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q=[root]#List with the root value
        ans=[]
        i=0
        while q:
            temp=[]
            tempAns=[]
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
     def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q=[root]#List with the root value
        ans=[]
        i=0
        direction = 'L'
        while q:
            temp=[]
            tempAns=[]
            for node in q :
                tempAns.append(node.key)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                q=temp
            if direction == 'L':
                ans.append(tempAns)
                direction = 'R'
            else:
                ans.append(tempAns[::-1])
                direction = 'L'
            q = temp
        return ans
root=Node(72)
root.insert(4)
root.insert(90)
root.insert(70)
root.insert(459)
root.insert(29)
print root.zigzagLevelOrder(root)



