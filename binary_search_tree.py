class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self,key):
        if not self.root:
            self.root = node(key)
        else:
            self._put(self.root,key)

    def _put(self,root,key):
        if key > root.key:
            if root.right:
                self._put(root.right,key)
            else:
                root.right = node(key)
        else:
            if root.left:
                self._put(root.left,key)
            else:
                root.left = node(key)
        
    def traversal(self):
        print('inorder: ',end='')
        self.inorder_traversal(self.root)
        print('\npreorder: ',end='')
        self.preorder_traversal(self.root)
        print('\npostorder: ',end='')
        self.postorder_traversal(self.root)
        print()
        

    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key,end=",")
            self.inorder_traversal(root.right)
    
    def preorder_traversal(self,root):
        if root:
            print(root.key,end=",")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
    
    def postorder_traversal(self,root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.key,end=",")

    
    def find_min(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node.key

    def find_max(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.key
        


tree = bst()
tree.put(8)
tree.put(3)
tree.put(10)
tree.put(1)
tree.put(6)
tree.put(14)
tree.put(4)
tree.put(7)
tree.put(13)
tree.traversal()
print(tree.find_min())
print(tree.find_max())
print("\nfininshed")
