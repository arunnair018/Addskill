class Graph(): 
    def __init__(self, v):
        self.vertices=[]
        for i in range(v):
            self.vertices.append(i)
        self.graph = [[0,5,0,9,2,0],
                    [5,0,2,0,0,0],
                    [0,2,0,3,0,0],
                    [9,0,3,0,0,2],
                    [2,0,0,0,0,3], 
                    [0,0,0,2,3,0]]
    
    def prims(self):
        MST={}
        visited=set()
        visited.add(self.vertices[0])
        while len(visited) < len(self.vertices):
            edges=[]
            for v1 in visited:
                for v2 in self.vertices:
                    if (v2 not in visited) and (self.graph[v1][v2]!=0):
                        edges.append([v1,v2,self.graph[v1][v2]])
            edges = sorted(edges,key=lambda x:x[2])
            MST[edges[0][0]] = (edges[0][1],edges[0][2])
            visited.add(edges[0][1])
        print(MST)
        
#x=int(input("No. of Nodes: "))
g  = Graph(6)
g.prims()
 
