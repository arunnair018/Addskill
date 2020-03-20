from collections import Counter
class graph:

    def __init__(self,directed = False):
        self.graph = {}
        self.directed = directed
        self.vertices = set()

    def _add(self,node1,node2):
        self.vertices.add(node1)
        self.vertices.add(node2)
        if node1 in self.graph:
            if node2 not in self.graph[node1]:
                self.graph[node1].append(node2)
            else:
                return ;
        else:
            self.graph[node1]=[node2]

        if not self.directed:
            self._add(node2,node1)
    
    def _show_graph(self):
        print(self.graph)
    
    def _dfs(self):
        stack,path = [list(self.graph.keys())[0]],[]
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            if vertex in self.graph:
                for i in self.graph[vertex]:
                    stack.append(i)
        return path

    def _bfs(self):
        q ,path = [list(self.graph.keys())[0]],[]
        while q:
            vertex = q.pop(0)
            if vertex in path:
                continue
            path.append(vertex)
            if vertex in self.graph:
                for i in self.graph[vertex]:
                    q.append(i)
        return path

    def _inorder(self):
        if self.directed==True:
            vertex = []
            if self.directed==True:
                for i in self.graph:
                    vertex+=self.graph[i]
            order = Counter(vertex)
            return dict(order)



    def _tsort(self):
        if self.directed==True:
            inorder = self._inorder()
            sort=[]
            root = list(self.graph.keys())[0]
            sort.append(root)
            while inorder:
                for i in self.graph[root]:
                    inorder[i]-=1
                root =  list(inorder.keys())[list(inorder.values()).index(0)]
                sort.append(root)
                del inorder[root]
        return sort



g = graph(directed=True)
g._add(1,2)
g._add(1,4)
g._add(2,3)
g._add(2,5)
g._add(2,4)
g._add(4,3)
g._add(4,6)
g._add(6,3)
g._add(5,3)
print('graph: ',end='')
g._show_graph()
print('bfs: ',g._bfs())
print('dfs: ',g._dfs())
print('toposort: ',g._tsort())