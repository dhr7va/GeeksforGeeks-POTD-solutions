#User function Template for python3

class Solution:
    def countWays(self, n, s):
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        mod = 1003
        
        for i in range(n - 1, -1, -2):
            for j in range(i, n, 2):
                if i == j:
                    dp[i][j][1] = 1 if s[i] == 'T' else 0
                    dp[i][j][0] = 1 if s[i] == 'F' else 0
                else:
                    for k in range(i, j, 2):
                        f1, f0 = dp[i][k][1], dp[i][k][0]
                        s1, s0 = dp[k + 2][j][1], dp[k + 2][j][0]
                        
                        if s[k + 1] == '&':
                            dp[i][j][1] = (dp[i][j][1] + (f1 * s1) % mod) % mod
                            dp[i][j][0] = (dp[i][j][0] + (f1 * s0) % mod + (f0 * s1) % mod + (f0 * s0) % mod) % mod
                        elif s[k + 1] == '|':
                            dp[i][j][1] = (dp[i][j][1] + (f1 * s0) % mod + (f0 * s1) % mod + (f1 * s1) % mod) % mod
                            dp[i][j][0] = (dp[i][j][0] + (f0 * s0) % mod) % mod
                        else:
                            dp[i][j][1] = (dp[i][j][1] + (f1 * s0) % mod + (f0 * s1) % mod) % mod
                            dp[i][j][0] = (dp[i][j][0] + (f1 * s1) % mod + (f0 * s0) % mod) % mod
        
        return dp[0][n - 1][1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends
