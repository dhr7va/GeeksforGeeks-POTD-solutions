#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        n = len(arr)
        count = 0
        
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends
