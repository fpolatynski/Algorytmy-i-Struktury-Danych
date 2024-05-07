import math
from graf_mst import graf

class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self) -> int:
            return hash(self.key)
        
    def __eq__(self, other) -> bool:
        return self.key == other
        
    def __repr__(self):
        return str(self.key)
        
        
class Edge:
    def __init__(self, weight = 0):
        self.weight = weight
    
    def __repr__(self):
        return str(self.weight)
        

class GraphList:
    def __init__(self):
        self.graph = {}
    
    def is_empty(self):
        return not bool(self.graph)
    
    def insert_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}
    
    def insert_edge(self, vertex1, vertex2, edge):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.graph[vertex1][vertex2] = edge
            
    def delete_vertex(self, vertex):
        if vertex in self.vertices():
            for keys in self.vertices():
                if vertex in self.graph[keys]:
                    del self.graph[keys][vertex]
                if keys in self.graph[vertex]:
                    del self.graph[vertex][keys]
            del self.graph[vertex]
                
    
    def delete_edge(self, vertex1, vertex2):
            del self.graph[vertex1][vertex2]
            del self.graph[vertex2][vertex1]
    
    def vertices(self):
        return list(self.graph.keys())
    
    def neighbours(self, vertex):
        if self.graph.get(vertex):
            return self.graph[vertex].items()
        else:
            return []
    
    def get_vertex(self, vertex):
        return vertex
    
class MST:
    def __init__(self, graph):
        self.g = graph
        self.mst = GraphList()
        self.intree = {x: 0 for x in graph.vertices()}
        self.parent = {x: 0 for x in graph.vertices()}
        self.distance = {x: math.inf for x in graph.vertices()}
        self.v = graph.vertices()[0]
        self.sum = 0
        
    def find_mst(self):
        while self.intree[self.v] == 0:
            self.intree[self.v] = 1
            for v, _ in self.g.neighbours(self.v):
                if not self.intree[v] and self.g.graph[self.v][v].weight < self.distance[v]:
                    self.distance[v] = self.g.graph[self.v][v].weight
                    self.parent[v] = self.v
            cur_min = math.inf
            min_v = None
            for v in self.g.vertices():
                if not self.intree[v]:
                    if self.distance[v] < cur_min:
                        min_v = v
                        cur_min = self.distance[v]
            if min_v is None:
                return self.mst
            else:
                self.mst.insert_edge(self.parent[min_v], min_v, self.g.graph[self.parent[min_v]][min_v])  
                self.mst.insert_edge(min_v, self.parent[min_v], self.g.graph[self.parent[min_v]][min_v])  
                self.v = min_v   
                self.sum +=  self.g.graph[self.parent[min_v]][min_v].weight
            
                
def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
    
              
def main():
    g = GraphList()
    for v1, v2, w in graf:
        g.insert_edge(Vertex(v1), Vertex(v2), Edge(w))
        g.insert_edge(Vertex(v2),Vertex(v1), Edge(w))
            
    mst = MST(g)
    g1 = mst.find_mst()
    printGraph(g1)

main()
    