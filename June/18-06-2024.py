#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        count = 0
        limit = 2 * r
        for l in range(1, limit + 1):
            for w in range(1, limit + 1):
                if l * l + w * w <= 4 * r * r:
                    count += 1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends
