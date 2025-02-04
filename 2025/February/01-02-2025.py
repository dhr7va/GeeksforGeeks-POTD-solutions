class Solution:
    def isWordExist(self, mat, word):
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or mat[i][j] != word[k]:
                return False
            
            temp, mat[i][j] = mat[i][j], '#'  # Mark as visited
            # Explore in all four directions
            found = any(dfs(i + dx, j + dy, k + 1) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)])
            mat[i][j] = temp  # Restore the character after visiting
            
            return found

        return any(dfs(i, j, 0) for i in range(len(mat)) for j in range(len(mat[0])) if mat[i][j] == word[0])




#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
