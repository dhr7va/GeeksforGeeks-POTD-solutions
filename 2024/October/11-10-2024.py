#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    def rearrange(self, arr):
        #Code here
        n = len(arr)
        
        for i in range(n):
            while 0 <= arr[i] < n and arr[i] != arr[arr[i]]:
                arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        
        for i in range(n):
            if arr[i] != i:
                arr[i] = -1
                
        return arr

#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        input_str = input()
        arr = list(map(int, input_str.split()))
        solution = Solution()
        ans = solution.rearrange(arr)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
# } Driver Code Ends
