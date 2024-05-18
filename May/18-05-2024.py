#User function Template for python3
from typing import List

class Solution:
	def findPeakElement(self, a):
		# Code here
        low = 0
        high = len(a) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            if a[mid] > a[mid + 1]:
                high = mid
            else:
                low = mid + 1
        
        return a[low]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends
