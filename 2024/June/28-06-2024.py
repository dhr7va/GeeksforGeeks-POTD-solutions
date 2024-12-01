#User function Template for python3

class Solution:
    def pattern (self, arr):
        # code here
        n = len(arr)
        
        def is_palindrome(sequence):
            return sequence == sequence[::-1]
        
        # Check rows
        for i in range(n):
            if is_palindrome(arr[i]):
                return "{} R".format(i)
        
        # Check columns
        for j in range(n):
            column = [arr[i][j] for i in range(n)]
            if is_palindrome(column):
                return "{} C".format(j)
        
        return "-1"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends
