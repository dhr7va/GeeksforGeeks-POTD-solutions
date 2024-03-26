#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# return 1 in case of True and 0 in case of False
class Solution:
    def isAdditiveSequence(self, n):
        #code here
        def is_valid(num1, num2, s):
            while s:
                next_num = str(int(num1) + int(num2))
                if not s.startswith(next_num):
                    return False
                s = s[len(next_num):]
                num1, num2 = num2, next_num
            return True

        for i in range(1, len(n)):  
            for j in range(1, len(n) - i):
                num1 = n[:i]
                num2 = n[i:i + j]
                if (num1.startswith('0') and len(num1) > 1) or (num2.startswith('0') and len(num2) > 1):
                    continue  
                if is_valid(num1, num2, n[i + j:]):
                    return 1
        return 0
        

#{ 
 # Driver Code Starts.
        
if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        s = input()
        print(sol.isAdditiveSequence(s))

# } Driver Code Ends
