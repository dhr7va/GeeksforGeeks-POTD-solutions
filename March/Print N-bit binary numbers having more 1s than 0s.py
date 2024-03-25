#User function Template for python3
class Solution:
    def NBitBinary(self, n):
        ans = []

        def permute(p, c, cur):
            nonlocal ans
            if c < p - c:
                return
            
            if p == n:
                ans.append(cur)
                return

            permute(p + 1, c + 1, cur + '1')
            permute(p + 1, c, cur + '0')

        permute(0, 0, '')
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends
