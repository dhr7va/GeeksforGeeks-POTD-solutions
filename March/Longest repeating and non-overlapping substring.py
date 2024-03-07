#User function Template for python3

class Solution:
    def longestSubstring(self, s , n):
        nax, i, j = 0, 0, 0
        out = "-1"
    
        while i < n and j < n:
            substring = s[i:j+1]
    
            if nax < len(substring) and s.find(substring, j + 1) != -1:
                nax = len(substring)
                out = substring
            else:
                i += 1
            j += 1
        
        return out

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S , N))
# } Driver Code Ends
