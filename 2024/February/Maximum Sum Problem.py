#User function Template for python3

class Solution:
    def maxSum(self, n): 
        # code here 
        if n <= 1:
            return n
        
        if n in self.dp:
            return self.dp[n]
        
        max_sum = max(n, self.maxSum(n // 2) + self.maxSum(n // 3) + self.maxSum(n // 4))
        
        self.dp[n] = max_sum
        
        return max_sum
    
    def __init__(self):
        self.dp = {}


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends
