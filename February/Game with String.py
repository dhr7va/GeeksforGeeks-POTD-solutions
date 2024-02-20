import heapq

class Solution:
    def minValue(self, s, k):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        pq = [(-count, char) for char, count in freq.items()]
        heapq.heapify(pq)
        
        for _ in range(k):
            if not pq:  
                break
            count, char = heapq.heappop(pq)
            count += 1
            if count < 0:
                heapq.heappush(pq, (count, char))
        
        min_value = sum(count ** 2 for count, _ in pq)
        
        return min_value
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends
