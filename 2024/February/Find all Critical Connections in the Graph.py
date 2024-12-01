class Solution:
    def __init__(self):
        self.time = 0

    def dfs(self, u, parent, disc, low, visited, adj, bridges):
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        visited[u] = True

        for v in adj[u]:
            if not visited[v]:
                self.dfs(v, u, disc, low, visited, adj, bridges)
                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridges.append((min(u, v), max(u, v)))
            elif v != parent:
                low[u] = min(low[u], disc[v])

    def criticalConnections(self, v, adj):
        disc = [-1] * v
        low = [-1] * v
        visited = [False] * v
        bridges = []

        for i in range(v):
            if not visited[i]:
                self.dfs(i, -1, disc, low, visited, adj, bridges)

        # Sorting the bridges for consistent output
        bridges.sort()

        return bridges

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends
