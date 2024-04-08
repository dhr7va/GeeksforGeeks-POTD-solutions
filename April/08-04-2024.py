#User function Template for python3


#Function to find the maximum possible amount of money we can win.
class Solution:
    def __init__(self):
        self.dp = []

    def solve(self, arr, i, j, n):
        if i >= n or j < 0 or j - i + 1 <= 0:
            return 0

        if self.dp[i][j] != -1:
            return self.dp[i][j]

        d1 = arr[i] + min(self.solve(arr, i + 2, j, n), self.solve(arr, i + 1, j - 1, n))
        d2 = arr[j] + min(self.solve(arr, i + 1, j - 1, n), self.solve(arr, i, j - 2, n))
        self.dp[i][j] = max(d1, d2)
        return self.dp[i][j]

    def optimalStrategyOfGame(self, n, arr):
        self.dp = [[-1] * 1001 for _ in range(1001)]
        return self.solve(arr, 0, n - 1, n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))

# } Driver Code Ends
