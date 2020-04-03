maxint=float('inf')
class Graph(): 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0,5,0,9,2,0],
                    [5,0,2,0,0,0],
                    [0,2,0,3,0,0],
                    [9,0,3,0,0,2],
                    [2,0,0,0,0,3], 
                    [0,0,0,2,3,0]]
    def printSolution(self, dist,src):
        print ("Vertex Distance from Source node ",src)
        for node in range(self.V):
            print (node,"node -----> ",dist[node])
    def minDistance(self, dist, sptSet):
        min = maxint
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    def dijkstra(self, src):
        dist = [maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist,src)
        
#x=int(input("No. of Nodes: "))
g  = Graph(6)
g.dijkstra(0)