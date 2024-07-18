#User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
       #code here
        if not arr:
            return 0
        
        inc = 1
        dec = 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                inc = dec + 1
            elif arr[i] < arr[i-1]:
                dec = inc + 1
        
        return max(inc, dec)

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)

# } Driver Code Ends
