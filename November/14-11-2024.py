#User function Template for python3

import heapq

class Solution:
    def nearlySorted(self, arr, k):
        heap = arr[:k + 1]
        heapq.heapify(heap)
        
        target_index = 0
        
        for i in range(k + 1, len(arr)):
            arr[target_index] = heapq.heappop(heap)
            target_index += 1
            
            heapq.heappush(heap, arr[i])
        
        while heap:
            arr[target_index] = heapq.heappop(heap)
            target_index += 1


#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        # print("~")
        t -= 1
# } Driver Code Ends
