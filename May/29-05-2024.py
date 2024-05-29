
class Solution:
    def findWinner(self, n: int, x: int, y: int) -> int:
        dp = [False] * (n + 1)
        
        dp[0] = False  
        
        for i in range(1, n + 1):
            if i >= 1 and not dp[i - 1]:
                dp[i] = True
            elif i >= x and not dp[i - x]:
                dp[i] = True
            elif i >= y and not dp[i - y]:
                dp[i] = True
            else:
                dp[i] = False
        
        return 1 if dp[n] else 0


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        obj = Solution()
        res = obj.findWinner(n, x, y)

        print(res)

# } Driver Code Ends
