from typing import List
import heapq

class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pq = [(0, 0, 0)]  # (effort, row, column)
        min_efforts = [[float('inf')] * columns for _ in range(rows)]
        min_efforts[0][0] = 0

        while pq:
            effort, row, col = heapq.heappop(pq)
            if row == rows - 1 and col == columns - 1:
                return effort
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < columns:
                    new_effort = max(effort, abs(heights[row][col] - heights[new_row][new_col]))
                    if new_effort < min_efforts[new_row][new_col]:
                        min_efforts[new_row][new_col] = new_effort
                        heapq.heappush(pq, (new_effort, new_row, new_col))

        return -1




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

        rows = int(input())

        columns = int(input())

        heights = IntMatrix().Input(rows, columns)

        obj = Solution()
        res = obj.MinimumEffort(rows, columns, heights)

        print(res)

# } Driver Code Ends
