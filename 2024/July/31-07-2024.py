#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        if not arr:
            return "-1"
        
        arr.sort()
        
        first = arr[0]
        last = arr[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        prefix = first[:i]
        
        return prefix if prefix else "-1"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends
