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
    def PreorderTraversal(self, roo):
        res = []
        if roo:
            res.append(roo.key)
            res = res + self.PreorderTraversal(roo.left)
            res = res + self.PreorderTraversal(roo.right)
        return res

    def PostorderTraversal(self, roo):
        res = []
        if roo:
            res = self.PostorderTraversal(roo.left)
            res = res + self.PostorderTraversal(roo.right)
            res.append(roo.key)
        return res
       



roo = Node(27)
roo.insert(14)
roo.insert(35)
roo.insert(10)
roo.insert(19)
roo.insert(31)
roo.insert(42)
print roo.PostorderTraversal(roo)
