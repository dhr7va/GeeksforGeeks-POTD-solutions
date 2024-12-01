#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        n = len(arr)
        
        for i in range(n - 1):
            if arr[i] == arr[i + 1] and arr[i] != 0:
                arr[i] = arr[i] * 2  
                arr[i + 1] = 0       
        
        result = []
        for num in arr:
            if num != 0:
                result.append(num)
        
        result.extend([0] * (n - len(result)))
        
        return result
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends
