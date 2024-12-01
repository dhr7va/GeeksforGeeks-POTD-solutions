#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        repeating = []
        
        for i in range(n + 2):
            index = abs(arr[i]) - 1
            if arr[index] < 0:
                repeating.append(abs(arr[i]))
            else:
                arr[index] = -arr[index]
        
        return repeating

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
