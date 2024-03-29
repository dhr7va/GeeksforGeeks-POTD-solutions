#User function Template for python3

from collections import deque

class Solution:
    def isEularCircuitExist(self, v, adj):
        if sum(len(vertex) for vertex in adj) == 0:
            return 1
        
        visited = [False] * v
        self.bfs(adj, 0, visited)
        if False in visited:
            return 0
        
        for vertex in adj:
            if len(vertex) % 2 != 0:
                return 0
        
        return 1
    
    def bfs(self, adj, start, visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

#{ 
 # Driver Code Starts
#Initial Template for python3

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
		ans = obj.isEularCircuitExist(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
