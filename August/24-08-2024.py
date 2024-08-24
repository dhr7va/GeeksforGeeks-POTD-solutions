#User function Template for python3

class Solution:
    
    def knapSack(self, W, wt, val):
        N = len(val)
        
        dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            for w in range(1, W + 1):
                if wt[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], val[i - 1] + dp[i - 1][w - wt[i - 1]])
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[N][W]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends
