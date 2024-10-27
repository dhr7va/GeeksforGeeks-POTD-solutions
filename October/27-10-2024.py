class Solution:
    def findTriplet(self, arr):
        arr.sort()
        n = len(arr)
        
        for i in range(n - 1, 1, -1):
            target = arr[i]
            left = 0
            right = i - 1
            
            while left < right:
                current_sum = arr[left] + arr[right]
                
                if current_sum == target:
                    return True
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends
