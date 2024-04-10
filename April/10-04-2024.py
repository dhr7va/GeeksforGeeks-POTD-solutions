#User function Template for python3

class Solution:
    def findSingle(self, n, arr):
        # code here
        single_person = 0
        for num in arr:
            single_person ^= num
        return single_person

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))

# } Driver Code Ends
