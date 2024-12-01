import heapq

class Solution:
    
    # Function to return the minimum cost to reach the bottom
    # right cell from the top left cell.
    def minimumCostPath(self, grid):
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        min_heap = [(grid[0][0], 0, 0)]
        
        cost = [[float('inf')] * n for _ in range(n)]
        cost[0][0] = grid[0][0]
        
        while min_heap:
            current_cost, x, y = heapq.heappop(min_heap)
            
            if x == n - 1 and y == n - 1:
                return current_cost
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n:
                    new_cost = current_cost + grid[nx][ny]
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heapq.heappush(min_heap, (new_cost, nx, ny))
        
        return -1

#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends
