import heapq
from collections import defaultdict
from typing import List

class Solution:
    def dijkstra(self, start: int, n: int, graph: List[List[int]]) -> List[int]:
        distances = [float('inf')] * n
        distances[start] = 0
        
        pq = [(0, start)]
        
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return distances
    
    def findCity(self, n: int, m: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for from_city, to_city, weight in edges:
            graph[from_city].append((to_city, weight))
            graph[to_city].append((from_city, weight))
        
        min_reachable = float('inf')
        city = -1
        
        for i in range(n):
            distances = self.dijkstra(i, n, graph)
            reachable = sum(1 for d in distances if d <= distanceThreshold)
            if reachable <= min_reachable:
                min_reachable = reachable
                city = i
        
        return city
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        
        n, m = map(int, input().strip().split())
        edges = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            edges.append([u, v, wt])
        distanceThreshold = int(input())
        obj = Solution()
        ans = obj.findCity(n, m, edges, distanceThreshold)
        print(ans)
            

# } Driver Code Ends
