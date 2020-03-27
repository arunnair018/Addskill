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
        print(self.no_of_v)
        print(self.vertices)
        print(self.graph)

    # to get the index of vertex 
    # which is not visited
    # and with min dist
    # from source 
    def minDistance(self, dist, visited,no_of_v):
        minint = float('inf')
        min_index=0
        for v in range(no_of_v):
            if dist[v] < minint and visited[v] == False:
                minint = dist[v]
                min_index = v
        return min_index

    def dijkstra(self,src):
        # sorting graph
        dgraph = dict(sorted(self.graph.items()))
        no_of_v = len(dgraph)
        # to keep track of minimum distance 
        dist = [float('inf')]*no_of_v
        # to keep track of visited nodes
        visited = [False]*no_of_v
        dist[src] = 0 
        
        for _ in range(no_of_v):
            # get node with minimum distance which is not visited
            u = self.minDistance(dist,visited,no_of_v)
            # make it visited
            visited[u] = True
            # traverse all neighbouring node
            for v in dgraph[u]:
                #if neighbour not visited
                if visited[v[0]] == False:
                    # update the distance if 
                    # distance till prev vertex + distance from 
                    # current node is less than the distance 
                    # in distance array.
                    if dist[v[0]] > dist[u] + v[1]:
                        dist[v[0]] = dist[u] + v[1]
        for i,j in enumerate(dist):
            print(src,' --> ',i,'= ',j)
        
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
g.dijkstra(1)
