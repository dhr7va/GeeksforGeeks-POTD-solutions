#User function Template for python3

class Solution:
    def sumSubstrings(self,s):
        mod = 10**9 + 7
        n = len(s)
        
        result = 0
        last_digit = 0
        
        for i in range(n):
            digit = int(s[i])
            
            last_digit = (last_digit * 10 + (i + 1) * digit) % mod
            result = (result + last_digit) % mod
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends
