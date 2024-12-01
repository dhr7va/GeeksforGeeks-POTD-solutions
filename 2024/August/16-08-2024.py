#User function Template for python3


class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            if i >= x and dp[i - x] != -1:
                dp[i] = max(dp[i], dp[i - x] + 1)
            if i >= y and dp[i - y] != -1:
                dp[i] = max(dp[i], dp[i - y] + 1)
            if i >= z and dp[i - z] != -1:
                dp[i] = max(dp[i], dp[i - z] + 1)
        
        return dp[n] if dp[n] != -1 else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends
