#User function Template for python3


class Solution:
    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"
        
        freq_p = {}
        for char in p:
            freq_p[char] = freq_p.get(char, 0) + 1
        
        required = len(freq_p)
        formed = 0
        
        left, right = 0, 0
        
        window_counts = {}
        
        ans = float("inf"), None, None
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in freq_p and window_counts[char] == freq_p[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window_counts[char] -= 1
                if char in freq_p and window_counts[char] < freq_p[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        if ans[0] == float("inf"):
            return "-1"
        else:
            return s[ans[1]: ans[2] + 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends
