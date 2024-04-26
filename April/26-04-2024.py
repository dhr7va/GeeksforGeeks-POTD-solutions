#User function Template for python3

class Solution:
    def FindExitPoint(self, n, m, matrix):
        row, col = 0, 0
        direction = 0  
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while 0 <= row < n and 0 <= col < m:
            current = matrix[row][col]
            
            if current == 1:
                direction = (direction + 1) % 4
                matrix[row][col] = 0
            
            delta_row, delta_col = directions[direction]
            row += delta_row
            col += delta_col
        
        row -= delta_row
        col -= delta_col
        
        return [row, col]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends
