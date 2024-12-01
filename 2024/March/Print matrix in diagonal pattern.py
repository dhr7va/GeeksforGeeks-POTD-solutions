# Your task is to complete this function

class Solution:
    def matrixDiagonally(self, mat):
        n = len(mat)
        res = []
        flag = False
        j = 0
        for row in range(n):
            r, c = row, 0
            temp = []
            while r >= 0 and c < n:
                temp.append(mat[r][c])
                r -= 1
                c += 1
            if flag:
                temp.reverse()
                flag = False
            else:
                flag = True
            res.extend(temp)
            j += len(temp)

        for col in range(1, n):
            r, c = n - 1, col
            temp = []
            while r >= 0 and c < n:
                temp.append(mat[r][c])
                r -= 1
                c += 1
            if flag:
                temp.reverse()
                flag = False
            else:
                flag = True
            res.extend(temp)
            j += len(temp)

        return res
#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
