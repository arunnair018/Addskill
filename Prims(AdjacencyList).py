from collections import OrderedDict
class graph:
    
    def __init__(self):
        self.graph = {}

    def _add(self,node1,node2,w):
        if node1 in self.graph:
            if (node2,w) not in self.graph[node1]:
                self.graph[node1].append((node2,w))
            else:
                return ;
        else:
            self.graph[node1]=[(node2,w)]

        self._add(node2,node1,w)
    
    def _show_graph(self):
        self.graph = dict(sorted(self.graph.items()))
        print(self.graph)

    def prims(self):
        vertices = list(self.graph.keys())
        MST = {}
        visited = set()
        visited.add(vertices[0])
        while len(visited) < len(vertices):
            edges=[]
            for v1 in visited:
                for v2 in self.graph[v1]:
                    if v2[0] not in visited:
                        edges.append((v1,v2))
            edges = sorted(edges,key=lambda x:x[1][1])
            MST[edges[0][0]] = (edges[0][1])
            visited.add(edges[0][1][0])
        print(MST)

#driver code
g = graph()
g._add(0,1,5)
g._add(0,3,9)
g._add(0,4,2)
g._add(1,2,2)
g._add(2,3,3)
g._add(3,5,2)
g._add(4,5,3)
#g._show_graph()
g.prims()