#User function Template for python3

class Solution:
    def minRow(self, n, m, a):
        min_ones = float('inf')  
        min_row_index = 1  
        
        for i in range(n):
            ones_count = sum(a[i])
            
            if ones_count < min_ones:
                min_ones = ones_count
                min_row_index = i + 1 
        
        return min_row_index

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends
