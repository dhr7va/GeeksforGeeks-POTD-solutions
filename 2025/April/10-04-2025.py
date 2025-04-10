#User function Template for python3
from heapq import heappush, heappop

class Solution:
    def minCost(self, houses):
        n = len(houses)
        visited = [False] * n
        min_heap = [(0, 0)]
        total_cost = 0

        while min_heap:
            cost, u = heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            total_cost += cost

            for v in range(n):
                if not visited[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    heappush(min_heap, (dist, v))

        return total_cost


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends
