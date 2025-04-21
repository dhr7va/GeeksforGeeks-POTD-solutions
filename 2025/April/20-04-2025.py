class Solution:
    def findDuplicate(self, arr):
        n = len(arr)
        actual_sum = sum(arr)
        expected_sum = (n - 1) * (n) // 2
        return actual_sum - expected_sum

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends
