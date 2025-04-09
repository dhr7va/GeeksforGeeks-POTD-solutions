class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict
        
        def dfs(u, parent):
            nonlocal time
            visited[u] = True
            disc[u] = low[u] = time
            time += 1
            children = 0

            for v in graph[u]:
                if not visited[v]:
                    children += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    if parent == -1 and children > 1:
                        ap.add(u)
                    if parent != -1 and low[v] >= disc[u]:
                        ap.add(u)
                elif v != parent:
                    low[u] = min(low[u], disc[v])

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * V
        low = [-1] * V
        visited = [False] * V
        ap = set()
        time = 0

        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        return sorted(ap) if ap else [-1]


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends
