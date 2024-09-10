#User function Template for python3
class Solution:
    def isCircle(self, arr):
        in_degree = [0] * 26
        out_degree = [0] * 26
        graph = [[] for _ in range(26)]
        
        def char_to_index(c):
            return ord(c) - ord('a')
        
        for word in arr:
            first_char = word[0]
            last_char = word[-1]
            start = char_to_index(first_char)
            end = char_to_index(last_char)
            
            out_degree[start] += 1
            in_degree[end] += 1
            graph[start].append(end)
        
        for i in range(26):
            if in_degree[i] != out_degree[i]:
                return 0
        
        def dfs(v, visited, graph):
            visited[v] = True
            for u in graph[v]:
                if not visited[u]:
                    dfs(u, visited, graph)
        
        start_vertex = -1
        for i in range(26):
            if out_degree[i] > 0:
                start_vertex = i
                break
        
        if start_vertex == -1:
            return 0
        visited = [False] * 26
        dfs(start_vertex, visited, graph)
        
        for i in range(26):
            if (in_degree[i] > 0 or out_degree[i] > 0) and not visited[i]:
                return 0
        
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()

        ob = Solution()
        print(ob.isCircle(A))

# } Driver Code Ends
