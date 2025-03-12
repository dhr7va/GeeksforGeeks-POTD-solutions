#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[-1], dp[-2])       


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends
