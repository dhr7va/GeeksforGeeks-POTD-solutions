from bisect import bisect_right

class Solution:
    def countPairs(self, arr, brr):
        brr.sort()
        count_y = [0] * 5
        for y in brr:
            if y < 5:
                count_y[y] += 1
        
        result = 0
        for x in arr:
            if x == 0:
                continue  
            elif x == 1:
                result += count_y[0]  
            else:
                index = bisect_right(brr, x)
                result += len(brr) - index
                
                result += count_y[1]
                
                if x == 2:
                    result -= count_y[3] + count_y[4]
                if x == 3:
                    result += count_y[2]
                    
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        # M, N = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countPairs(a, b))
        #code here

# } Driver Code Ends
