#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# from typing import List


class Solution:
    def rotateDelete(self,  arr):
        # code here
        n = len(arr)
        for k in range(1, n // 2 + 1):
            arr = [arr[-1]] + arr[:-1]
            
            to_delete = len(arr) - k  
            arr.pop(to_delete)
        
        return arr[0]


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1


# } Driver Code Ends
