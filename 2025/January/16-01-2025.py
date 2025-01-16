class Solution:
    def maxLen(self, arr):
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = -1
        
        prefix_sum_map = {}
        prefix_sum = 0
        max_length = 0
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum == 0:
                max_length = i + 1
            
            if prefix_sum in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[prefix_sum])
            else:
                prefix_sum_map[prefix_sum] = i
        
        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends
