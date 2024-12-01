#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        max_sum = float('-inf') 
        current_sum = 0 
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends