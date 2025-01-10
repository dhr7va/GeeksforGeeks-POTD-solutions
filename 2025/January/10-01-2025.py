
from collections import defaultdict

class Solution:
    def countDistinct(self, arr, k):
        freq = defaultdict(int)
        result = []
        distinct_count = 0
        
        for i in range(k):
            if freq[arr[i]] == 0:
                distinct_count += 1
            freq[arr[i]] += 1
        
        result.append(distinct_count)
        
        for i in range(k, len(arr)):
            outgoing = arr[i - k]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                distinct_count -= 1
            
            incoming = arr[i]
            if freq[incoming] == 0:
                distinct_count += 1
            freq[incoming] += 1
            
            result.append(distinct_count)
        
        return result
        
#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends
