
from typing import List


class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        # code here
        if n == 0 or m == 0:
            return 0
        
        dp = [[0] * m for _ in range(n)]
        max_side_length = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side_length = max(max_side_length, dp[i][j])
        
        return max_side_length        



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

        n, m = map(int, input().split())

        mat = IntMatrix().Input(n, m)

        obj = Solution()
        res = obj.maxSquare(n, m, mat)

        print(res)

# } Driver Code Ends
