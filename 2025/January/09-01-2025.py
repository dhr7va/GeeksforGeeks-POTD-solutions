#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        left = 0
        current_sum = 0
        
        for right in range(len(arr)):
            current_sum += arr[right]
            
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
            
            if current_sum == target:
                return [left + 1, right + 1]
        
        return [-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends
