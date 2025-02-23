# User function Template for python3

class Solution:
    def nextLargerElement(self, arr):
        s = []
        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]
            while s and s[-1] <= val:
                s.pop()
            arr[i] = -1 if not s else s[-1]
            s.append(val)
        return arr
        
        
#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends
