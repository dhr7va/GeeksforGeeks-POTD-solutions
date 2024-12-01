class Solution:
    def rotateMatrix(self, k, mat):
        n = len(mat)  
        m = len(mat[0])  
        
        k = k % m
        
        rotated_matrix = []
        
        for i in range(n):
            new_row = mat[i][k:] + mat[i][:k]
            rotated_matrix.append(new_row)
        
        return rotated_matrix


#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends
