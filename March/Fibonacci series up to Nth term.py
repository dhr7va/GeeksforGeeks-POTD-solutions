#User function Template for python3

class Solution:
    def series(self, n):
        MOD = 10**9 + 7
        fib = [0] * (n + 1)
        fib[0] = 0
        fib[1] = 1

        for i in range(2, n + 1):
            fib[i] = (fib[i - 1] + fib[i - 2]) % MOD

        return fib
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends
