class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def ConstructTree(arr,root,i,n):
    if i < n:
        if arr[i] is not None:
            temp = Node(arr[i])
            root = temp

            root.left = ConstructTree(arr,root.left,2*i+1,n)
            root.right = ConstructTree(arr,root.right,2*i+2,n)
        return root

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val,end=' ')
        Inorder(root.right)

def bfs(root):
    q = [root]
    while q:
        lenght = len(q)
        for i in range(lenght):
            node = q.pop(0)
            print(node.val,end=' ')
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

# driver code
a = [1,2,3,4,None,6]
root=None
root = ConstructTree(a,root,0,len(a))
print('inorder: ',end=' ')
Inorder(root)
print('\nBFS: ',end=' ')
bfs(root)
print()
    