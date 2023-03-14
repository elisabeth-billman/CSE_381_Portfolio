from collections import defaultdict
 
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        # Alternative to defaultdict
        # self.graph = {}
        # for i in range(vertices):
        #     self.graph[i] = []
        self.V = 0
 
    def addEdge(self, u, v):
        self.V += 1
        self.graph[u].append(v)
 
    # A recursive function used to sort
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        
        # Check adjacent vertices
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
 
        stack.insert(0,v)
        print(stack)

    # This function only runs once
    def topological_sort(self):
        visited = [False] * self.V
        stack =[]
        print(self.graph.items())
 
        # Call the recursive helper function for each vertice
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
 
g = Graph()

g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(5, 0)
g.addEdge(5, 2)
g.addEdge(4, 0)
g.addEdge(3, 1)

g.topological_sort()
