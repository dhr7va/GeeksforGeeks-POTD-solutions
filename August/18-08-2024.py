class Solution:
    def canSplit(self, arr):
        #code here
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2
        current_sum = 0
        
        for num in arr:
            current_sum += num
            if current_sum == target_sum:
                return True
        
        return False

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends
