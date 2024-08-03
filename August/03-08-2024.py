class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        a = 0
        b = n - 1
        
        while a < b:
            if mat[a][b] == 1:
                a += 1
            else:
                b -= 1
        
        candidate = a
        
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        
        return candidate

#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends
