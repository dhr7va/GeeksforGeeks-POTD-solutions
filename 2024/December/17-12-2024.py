#User function Template for python3


class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        
        def canPlaceCows(minDist):
            count = 1  
            last_pos = stalls[0]  
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_pos >= minDist:
                    count += 1  
                    last_pos = stalls[i]  
                    if count >= k:  
                        return True
            return False

        
        left = 1  
        right = stalls[-1] - stalls[0]  
        res = 0  
        
        while left <= right:
            mid = (left + right) // 2  
            if canPlaceCows(mid):  
                res = mid  
                left = mid + 1  
            else:
                right = mid - 1  
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends
