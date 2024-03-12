#User function Template for python3

class Solution:
    def multiply(self, res, mat, m):
        res1 = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    res1[i][j] += (res[i][k] * mat[k][j]) % m
        for i in range(3):
            for j in range(3):
                res[i][j] = res1[i][j]

    def mat_exp(self, n, m):
        while n > 0:
            if n & 1:
                self.multiply(self.res, self.mat, m)
            self.multiply(self.mat, self.mat, m)
            n //= 2

    def genFibNum(self, a, b, c, n, m):
        self.res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.res[0][0] = self.res[1][1] = self.res[2][2] = 1
        self.mat = [[a, b, 1], [1, 0, 0], [0, 0, 1]]
        if n <= 2:
            return 1 % m
        else:
            self.mat_exp(n - 2, m)
            return (self.res[0][0] + self.res[0][1] + c * self.res[0][2]) % m        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b,c,n,m=map(int,input().split())
        
        ob = Solution()
        print(ob.genFibNum(a,b,c,n,m))
# } Driver Code Ends
