#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]
        
        i, j, k = 0, 0, 0
        
        while i < len(pos) and j < len(neg):
            if k % 2 == 0:
                arr[k] = pos[i]
                i += 1
            else:
                arr[k] = neg[j]
                j += 1
            k += 1
        
        while i < len(pos):
            arr[k] = pos[i]
            i += 1
            k += 1
        
        while j < len(neg):
            arr[k] = neg[j]
            j += 1
            k += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
