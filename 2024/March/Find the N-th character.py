#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        # Precompute the transformations to avoid repetitive string operations
        transformation = {'1': '10', '0': '01'}
        
        for _ in range(r):
            # Transform each character according to the rules
            s = ''.join(transformation[char] for char in s)
            # If the length of the transformed string exceeds n, no need to keep the rest
            if len(s) > n:
                s = s[:n+1]
                
        return s[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends
