#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        repeating = -1
        missing = -1
        
        for i in range(n):
            if arr[abs(arr[i]) - 1] < 0:
                repeating = abs(arr[i])  
            else:
                arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

        for i in range(n):
            if arr[i] > 0:
                missing = i + 1
                break
        
        return [repeating, missing]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends
