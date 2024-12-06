#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n = len(citations)
        
        count = [0] * (n + 1)
        
        for c in citations:
            if c >= n:
                count[n] += 1  
            else:
                count[c] += 1
        
        h = 0  
        for i in range(n, -1, -1):
            h += count[i]  
            if h >= i: 
                return i
        
        return 0

#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends
