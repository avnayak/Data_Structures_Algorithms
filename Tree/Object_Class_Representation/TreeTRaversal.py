class Node(object):

    def __init__(self, root):

        self.key = root
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
    def inorderTraversal(self, roo):
        res = []
        if roo:
            res = self.inorderTraversal(roo.left)
            res.append(roo.key)
            res = res + self.inorderTraversal(roo.right)
        return res
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.key)
        return res
       



roo = Node(27)
roo.insert(14)
roo.insert(35)
roo.insert(10)
roo.insert(19)
roo.insert(31)
roo.insert(42)
print roo.PostorderTraversal(roo)
