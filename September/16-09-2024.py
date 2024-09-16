# User function Template for Python3

class Solution:
    def maxLength(self, str):
        # code here
        stack = []
        stack.append(-1)
        max_len = 0
        
        for i in range(len(str)):
            if str[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if len(stack) != 0:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        
        return max_len

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))

# } Driver Code Ends
