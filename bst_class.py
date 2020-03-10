class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class bst:
    # initialize tree structure
    def __init__(self):
        self.root = None
        self.size = 0
    # insert value into the tree
    def insert(self,key):
        # if tree is empty
        if not self.root:
            self.root = node(key)
        else:
            self._insert(self.root,key)

    def _insert(self,root,key):
        # if value is greater than current node value
        if key > root.key:
            if root.right:
                self._insert(root.right,key)
            else:
                root.right = node(key)
        # if value is less than current node value
        else:
            if root.left:
                self._insert(root.left,key)
            else:
                root.left = node(key)
    
    # traverse throughout the tree
    def traversal(self):
        print('inorder: ',end='')
        self.inorder_traversal(self.root)
        print('\npreorder: ',end='')
        self.preorder_traversal(self.root)
        print('\npostorder: ',end='')
        self.postorder_traversal(self.root)
        print()
        
    # traverse inorder,
    # go left, print value, go right 
    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key,end=",")
            self.inorder_traversal(root.right)
    
    # traverse preorder
    # print value, go left, go right 
    def preorder_traversal(self,root):
        if root:
            print(root.key,end=",")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
    
    # traverse postorder
    # go left, go right, print value
    def postorder_traversal(self,root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.key,end=",")

    # function to find the minimum value in the tree
    def find_min(self):
        return self._min(self.root).key

    def _min(self,ptr):
        # traverse to the left deepest node
        while ptr.left is not None:
            ptr = ptr.left
        return ptr

    # function to find the maximum value in the tree
    def find_max(self):
        return self._max(self.root).key

    def _max(self,ptr):
        # traverse to the right deepest node
        while ptr.right is not None:
            ptr = ptr.right
        return ptr

    # function to delete a node
    def delete(self,del_key):
        return self._delete(self.root,del_key)    

    def _delete(self,root,del_key):
        if root is None:
            return root
        
        # if key is less than root
        if del_key < root.key:
            root.left = self._delete(root.left,del_key)
        
        # if key is greater than root
        elif del_key > root.key:
            root.right = self._delete(root.right,del_key)
        
        # if key is found
        else:
            # if node got one or no child
            if root.left is None : 
                temp = root.right  
                root = None 
                return temp  
                
            elif root.right is None : 
                temp = root.left  
                root = None
                return temp 
            # for node with two children. get the successor.
            temp = self._min(root.right)
            # swap successor with node
            root.key = temp.key
            #delete the successor
            root.right = self._delete(root.right,temp.key)
        return root

