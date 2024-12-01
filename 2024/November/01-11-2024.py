#User function Template for python3

class Solution:
    def maxSum(self, arr):
        arr.sort()
        
        n = len(arr)
        rearranged = []
        i, j = 0, n - 1
        while i <= j:
            if i == j:
                rearranged.append(arr[i])
            else:
                rearranged.append(arr[i])
                rearranged.append(arr[j])
            i += 1
            j -= 1
        
        max_sum = 0
        for k in range(1, n):
            max_sum += abs(rearranged[k] - rearranged[k - 1])
        
        max_sum += abs(rearranged[n - 1] - rearranged[0])
        
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
