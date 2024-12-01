#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    def kadane(nums):
        max_ending_here = max_so_far = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    n = len(arr)
    
    max_kadane = kadane(arr)
    
    total_sum = sum(arr)
    inverted_arr = [-x for x in arr]
    max_wrap = total_sum + kadane(inverted_arr)  
    
    if max_wrap == 0:
        return max_kadane
    
    return max(max_kadane, max_wrap)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends
