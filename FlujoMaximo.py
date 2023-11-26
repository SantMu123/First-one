from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, 0])  # Agregar una arista de retorno con capacidad cero

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for index, [v, capacity] in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = (u, index)

        return True if visited[t] else False

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink

            while s != source:
                parent_node, index = parent[s]
                path_flow = min(path_flow, self.graph[parent_node][index][1])
                s = parent_node

            max_flow += path_flow
            v = sink

            while v != source:
                u, index = parent[v]
                self.graph[u][index][1] -= path_flow
                self.graph[v][0][1] += path_flow
                v = u

        return max_flow

# Ejemplo de uso:
g = Graph(6)
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

source = 0
sink = 5

max_flow = g.edmonds_karp(source, sink)
print(f"El flujo máximo en la red es: {max_flow}")