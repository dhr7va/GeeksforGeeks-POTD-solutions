#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        reversed_binary = 0
        bit_length = 32  
        for i in range(bit_length):
            reversed_binary |= ((x >> i) & 1) << (bit_length - i - 1)
        
        return reversed_binary


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends
