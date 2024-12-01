#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n): 
    #Your code here
        if n == 0 or n == 1:
            return n
        
        start = 1
        end = n
        result = 0
        
        while start <= end:
            mid = (start + end) // 2
            
            if mid * mid == n:
                return mid
            
            if mid * mid < n:
                start = mid + 1
                result = mid
            else:
                end = mid - 1
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
