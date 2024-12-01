#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        # code here 
        high_nibble = (n & 0xF0) >> 4
        low_nibble = (n & 0x0F) << 4
        
        swap_nibbles = high_nibble | low_nibble
        
        return swap_nibbles
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends
