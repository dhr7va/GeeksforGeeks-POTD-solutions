class Solution:
    def nQueen(self, n):
        def isSafe(board, row, col):
            for i in range(row):
                if board[i] == col:
                    return False
            
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i] == j:
                    return False
            
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i] == j:
                    return False
            
            return True

        def solveNQueens(board, row):
            if row == n:
                result.append([col + 1 for col in board])
                return
            
            for col in range(n):
                if isSafe(board, row, col):
                    board[row] = col
                    solveNQueens(board, row + 1)
                    board[row] = -1 

        result = []
        board = [-1] * n
        solveNQueens(board, 0)

        return result





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends
