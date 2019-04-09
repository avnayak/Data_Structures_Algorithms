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
    
    
    
     def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        depth = 0
        q = [root]
        #while len(q) != 0:
        while q:
            depth += 1
            for i in range(0, len(q)):
                if not q[0].left and not q[0].right:
                    return depth
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                del q[0]

        return depth
root=Node(72)
root.insert(4)
root.insert(90)
root.insert(70)
root.insert(459)
root.insert(29)
print root.minDepth(root)
