class Solution:
	def editDistance(self, str1, str2):
		# Code here
        m, n = len(str1), len(str2)
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                
                if i == 0:
                    dp[i][j] = j    
                
                elif j == 0:
                    dp[i][j] = i    
                
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],    
                                       dp[i-1][j],    
                                       dp[i-1][j-1])  
        
        return dp[m][n]


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends
