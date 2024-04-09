#User function Template for python3
class Solution:
	def minPoints(self, m, n, points):
		# code here
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n] = 1
        dp[m][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                minPointsNeeded = min(dp[i + 1][j], dp[i][j + 1]) - points[i][j]
                dp[i][j] = max(1, minPointsNeeded)

        return dp[0][0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m,n = int(m),int(n)
		points = []
		for _ in range(m):
			temp = [int(x) for x in input().split()]
			points.append(temp)
		ob = Solution()
		ans = ob.minPoints(m,n,points)
		print(ans)




# } Driver Code Ends
