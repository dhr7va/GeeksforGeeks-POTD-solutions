#User function Template for python3
class Solution:
	def maxDotProduct(self, n, m, a, b):
		# code here
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for j in range(1, m + 1):
            dp[0][j] = float('-inf')
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1] * b[j - 1])
        
        return dp[n][m]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n,m = int(n),int(m)
		a = [int(x) for x in input().split()]
		b = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxDotProduct(n,m,a,b)
		print(ans)
# } Driver Code Ends
