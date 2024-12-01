#User function Template for python3

class Solution:
    def sequence(self, n):
        MOD = 10**9 + 7
        result = 0
        current_term = 1
        for i in range(1, n + 1):
            product = 1
            for j in range(i):
                product *= current_term
                current_term += 1
            result += product
            result %= MOD
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends
