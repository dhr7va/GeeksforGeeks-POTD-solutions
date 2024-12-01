#User function Template for python3
class Solution:
    def findMinCost(self, x, y, costX, costY):
        m = len(x)
        n = len(y)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            dp[i][0] = i * costX
        for j in range(1, n + 1):
            dp[0][j] = j * costY
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + costX, dp[i][j - 1] + costY)
        
        return dp[m][n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        X, Y, costX, costY = input().split()
        costX = int(costX)
        costY = int(costY)
        ob = Solution()
        ans = ob.findMinCost(X, Y, costX, costY)
        print(ans)

# } Driver Code Ends
