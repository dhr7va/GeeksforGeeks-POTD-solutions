#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
        curr_max = arr[0]
        curr_min = arr[0]
        max_product = arr[0]

        for i in range(1, len(arr)):
            if arr[i] < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(arr[i], curr_max * arr[i])
            curr_min = min(arr[i], curr_min * arr[i])

            max_product = max(max_product, curr_max)

        return max_product
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
