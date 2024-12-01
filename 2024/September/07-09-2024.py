#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        result = 0
        power = 1
        
        while n > 0:
            result += (n % 9) * power
            n //= 9
            power *= 10
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends
