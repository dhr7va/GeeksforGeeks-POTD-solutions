#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:
    def maxPathSum(self, arr1, arr2):
        # Code here
        i, j = 0, 0
        sum1, sum2, result = 0, 0, 0
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                result += max(sum1, sum2) + arr1[i]
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1
        
        while i < len(arr1):
            sum1 += arr1[i]
            i += 1
        
        while j < len(arr2):
            sum2 += arr2[j]
            j += 1
        
        result += max(sum1, sum2)
        
        return result

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends
