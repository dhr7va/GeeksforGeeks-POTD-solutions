#User function Template for python3

class Solution:
    def lis(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and (nums[i] - nums[j]) >= (i - j):
                    dp[i] = max(1 + dp[j], dp[i])
                    
        out = 1
        for i in dp:
            out = max(out, i)
        
        return out
    
    def min_operations(self, nums):
        return len(nums) - self.lis(nums)
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.min_operations(nums)
		print(ans)
# } Driver Code Ends
