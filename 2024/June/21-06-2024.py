#User function Template for python3


class Solution:
    def compareFrac (self, str):
        
        # code here
        parts = str.split(", ")
        
        frac1 = parts[0].split("/")
        frac2 = parts[1].split("/")
        
        a = int(frac1[0])
        b = int(frac1[1])
        c = int(frac2[0])
        d = int(frac2[1])
        
        if a * d > b * c:
            return "{}/{}".format(a, b)
        elif a * d < b * c:
            return "{}/{}".format(c, d)
        else:
            return "equal"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends
