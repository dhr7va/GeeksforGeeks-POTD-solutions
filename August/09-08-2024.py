#User function Template for python3

class Solution:
    def Maximize(self, arr): 
        # Complete the function
        MOD = 10**9 + 7
        
        arr.sort()
        
        max_sum = 0
        
        for i in range(len(arr)):
            max_sum += arr[i] * i
            max_sum %= MOD  
        
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends
