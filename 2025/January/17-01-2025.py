#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here

        n = len(arr)
        if n == 2:
            return [arr[1], arr[0]]
        
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= arr[i]
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends
