#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        low = max(1, q - n)
        high = min(n, q - 1)
        
        if low > high:
            return 0
        else:
            return high - low + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends
