#User function Template for python3
class Solution:
    def countPairs(self, mat1, mat2, n, x):
        h1 = set()
        h2 = set()
        pair = 0

        for i in range(n):
            for j in range(n):
                h1.add(mat1[i][j])

        for i in range(n):
            for j in range(n):
                h2.add(mat2[i][j])

        for v in h1:
            if x - v in h2:
                pair += 1

        return pair

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends
