class Solution:
    def dfs(self, graph, u, visited):
        visited[u] = True
        for v in range(len(graph)):
            if graph[u][v] == 1 and not visited[v]:
                self.dfs(graph, v, visited)

    def isPossible(self, paths):
        n = len(paths)
        graph = paths
        
        # Counting the degree of each node
        degree = [sum(row) for row in graph]
        
        # Checking if each node has an even degree
        for d in degree:
            if d % 2 != 0:
                return "Not Possible"

        # Checking if the graph is connected
        visited = [False] * n
        self.dfs(graph, 0, visited)
        if not all(visited):
            return "Not Possible"

        return "Possible"
