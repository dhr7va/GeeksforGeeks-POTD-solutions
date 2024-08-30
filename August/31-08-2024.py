#User function Template for python3



class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n = len(arr)
        if n < 3:
            return []
        
        left_min = [0] * n
        right_max = [0] * n
        
        left_min[0] = float('inf')
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], arr[i - 1])
        
        right_max[n - 1] = float('-inf')
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i + 1])
        
        for j in range(1, n - 1):
            if left_min[j] < arr[j] < right_max[j]:
                return [left_min[j], arr[j], right_max[j]]
        
        return []

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def isSubSequence(v1, v2):
    m = len(v2)
    n = len(v1)
    j = 0  # For index of v2
    # Traverse v1 and v2
    for i in range(n):
        if j < m and v1[i] == v2[j]:
            j += 1
    return j == m


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        n = len(arr)
        obj = Solution()
        res = obj.find3Numbers(arr)
        if len(res) != 0 and len(res) != 3:
            print(-1)
        else:
            if not res:
                print(0)
            elif res[0] < res[1] < res[2] and isSubSequence(arr, res):
                print(1)
            else:
                print(-1)

# } Driver Code Ends
