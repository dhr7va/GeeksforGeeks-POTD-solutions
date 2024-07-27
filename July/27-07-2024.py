#User function Template for python3

class Solution:
    def countMin(self, str):
        # code here
        n = len(str)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if str[i] == str[j] and cl == 2:
                    dp[i][j] = 2
                elif str[i] == str[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        
        lps = dp[0][n - 1]

        return n - lps
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))

# } Driver Code Ends
