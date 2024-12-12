class Solution:
    def countFreq(self, arr, target):
        #code here
        left_index = bisect.bisect_left(arr, target)
        
        if left_index == len(arr) or arr[left_index] != target:
            return 0

        right_index = bisect.bisect_right(arr, target)
        
        return right_index - left_index

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
