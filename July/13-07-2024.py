#User function Template for python3
from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n + 1)]
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        pq = [(0, 1)]  
        dist = [float('inf')] * (n + 1)
        dist[1] = 0
        parent = [-1] * (n + 1)
        parent[1] = 0
        
        while pq:
            current_dist, node = heapq.heappop(pq)
            
            if current_dist > dist[node]:
                continue
            
            for neighbor, weight in graph[node]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
                    parent[neighbor] = node
        
        if dist[n] == float('inf'):
            return [-1]
        
        path = []
        current = n
        while current != 0:
            path.append(current)
            current = parent[current]
        
        path.reverse()
        
        return [dist[n]] + path


#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends
