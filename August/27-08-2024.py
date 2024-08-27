class Solution:
    def findMaxDiff(self, arr):
        # code here
        n = len(arr)
        ls = [0] * n  
        rs = [0] * n  
        

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                ls[i] = arr[stack[-1]]
            else:
                ls[i] = 0
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                rs[i] = arr[stack[-1]]
            else:
                rs[i] = 0
            stack.append(i)

        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(ls[i] - rs[i]))
        
        return max_diff

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends
