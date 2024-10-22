#User function Template for python3

class Solution:
    def sameOccurrence(self, arr, x, y):
        # code here
        diff = 0
        diff_map = {0: 1}  
        count = 0
        
        for num in arr:
            if num == x:
                diff += 1
            elif num == y:
                diff -= 1
            

            if diff in diff_map:
                count += diff_map[diff]
            
            if diff in diff_map:
                diff_map[diff] += 1
            else:
                diff_map[diff] = 1
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends
