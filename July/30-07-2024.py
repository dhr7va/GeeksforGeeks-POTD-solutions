from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # code here
        def is_safe(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1

        def solve(x, y, path):
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return

            m[x][y] = 0
            
            for move_x, move_y, move_char in [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]:
                next_x, next_y = x + move_x, y + move_y
                if is_safe(next_x, next_y):
                    solve(next_x, next_y, path + move_char)
            
            m[x][y] = 1
        
        if not m or m[0][0] == 0:
            return []
        
        n = len(m)
        paths = []
        
        solve(0, 0, "")
        
        return paths



#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends
