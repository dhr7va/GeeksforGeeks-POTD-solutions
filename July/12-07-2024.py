from typing import List, Tuple

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def is_valid(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < n
        
        def dfs(x: int, y: int, visited: List[List[bool]], label: int) -> int:
            stack = [(x, y)]
            visited[x][y] = True
            grid[x][y] = label
            size = 0
            while stack:
                cx, cy = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if is_valid(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        grid[nx][ny] = label
                        stack.append((nx, ny))
            return size
        
        label = 2  
        visited = [[False] * n for _ in range(n)]
        component_size = {}
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    size = dfs(i, j, visited, label)
                    component_size[label] = size
                    label += 1
        
        max_size = max(component_size.values()) if component_size else 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_labels = set()
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if is_valid(nx, ny) and grid[nx][ny] > 1:
                            neighbor_labels.add(grid[nx][ny])
                    
                    new_size = 1  
                    for label in neighbor_labels:
                        new_size += component_size[label]
                    
                    max_size = max(max_size, new_size)
        
        return max_size   



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.MaxConnection(grid)

        print(res)

# } Driver Code Ends
