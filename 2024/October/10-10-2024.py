class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        first_occurrence = {}
        max_dist = 0

        # Traverse the array
        for i in range(len(arr)):
            if arr[i] not in first_occurrence:
                first_occurrence[arr[i]] = i
            else:
                dist = i - first_occurrence[arr[i]]
                max_dist = max(max_dist, dist)

        return max_dist


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends
