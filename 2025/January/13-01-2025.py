
class Solution:
    def maxWater(self, arr):
        # code here
        left = 0
        right = len(arr) - 1
        max_area = 0
        
        while left < right:
            height = min(arr[left], arr[right])
            width = right - left
            current_area = height * width
            
            max_area = max(max_area, current_area)
            
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
