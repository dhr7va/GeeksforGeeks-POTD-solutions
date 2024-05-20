#User function Template for python3

class Solution:
    def PowMod(self, x, n, m):
        result = 1
        x = x % m  

        if x == 0:
            return 0  

        while n > 0:
            if (n & 1) == 1:
                result = (result * x) % m

            n = n >> 1  
            x = (x * x) % m  

        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends
