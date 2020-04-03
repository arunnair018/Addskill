from collections import defaultdict

class graph:
    def __init__(self):
        self.vertices = []
        self.graph = []

    def add(self,u,v,w):
        self.graph.append([u,v,w])
    
    def kruskal(self):
        result = []
        

'''
g = [('s','a',7),
    ('s','c',8),
    ('a','c',3),
    ('a','b',6),
    ('c','b',4),
    ('c','d',3),
    ('b','d',2),
    ('b','t',5),
    ('d','t',2),
    ('a','b',9),]
'''