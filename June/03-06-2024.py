#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes(self, n):
        MOD = 10**9 + 7
        
        if n == 1:
            return 0
        
        dp0 = [0] * (n + 1)
        dp1 = [0] * (n + 1)
        
        dp0[1] = 1
        dp1[1] = 1
        
        for i in range(2, n + 1):
            dp0[i] = (dp0[i-1] + dp1[i-1]) % MOD
            dp1[i] = dp0[i-1]
        
        total_without_consecutive_ones = (dp0[n] + dp1[n]) % MOD
        
        total_binary_strings = pow(2, n, MOD)
        
        result = (total_binary_strings - total_without_consecutive_ones + MOD) % MOD
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends
