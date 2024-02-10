#User function Template for python3

class Solution:
    def numberOfPath (self, n, k, arr):
        dr = [1, 0]
        dc = [0, 1]  
        
        def valid(x, y):
            return 0 <= x < n and 0 <= y < n
        
        dp = [[[None] * (k + 1) for _ in range(n)] for _ in range(n)]
        
        def helper(r, c, s):
            if r == n - 1 and c == n - 1:
                return int(s == arr[r][c])
            
            if dp[r][c][s] is not None:
                return dp[r][c][s]
            
            dp[r][c][s] = 0
            
            if arr[r][c] <= s:
                for d in range(2):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    
                    if valid(nr, nc):
                        dp[r][c][s] += helper(nr, nc, s - arr[r][c])
            
            return dp[r][c][s]
        
        return helper(0, 0, k)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        k= int(input())
        n=int(input())
        l = list(map(int, input().split()))
        arr = list()
        c=0
        for i in range(0, n):
            temp = list()
            for j in range(0, n):
                temp.append(l[c])
                c += 1
            arr.append(temp)
        ans = ob.numberOfPath(n, k, arr);
        print(ans)


# } Driver Code Ends
