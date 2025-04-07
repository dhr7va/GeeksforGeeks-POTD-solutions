
class Solution:
    def isCycle(self, V, edges):
        from collections import defaultdict

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V
        recStack = [False] * V  

        def dfs(v):
            visited[v] = True
            recStack[v] = True

            for neighbour in adj[v]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True
                elif recStack[neighbour]:
                    return True  

            recStack[v] = False
            return False

        for node in range(V):
            if not visited[node]:
                if dfs(node):
                    return True
        return False


#{ 
 # Driver Code Starts
from collections import deque


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")


if __name__ == "__main__":
    main()

# } Driver Code Ends
