class Solution:
    def alternateSort(self, arr):
        # Sort the array in ascending order
        arr.sort()
        result = []
        
        left, right = 0, len(arr) - 1
        
        while left <= right:
            if left != right:
                result.append(arr[right])  
                result.append(arr[left])   
            else:
                result.append(arr[left])   
            right -= 1
            left += 1
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
