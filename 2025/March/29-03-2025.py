class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        jobs = sorted(zip(profit, deadline), reverse=True, key=lambda x: x[0])
        

        max_deadline = max(deadline)
        parent = list(range(max_deadline + 1))  
        
        def find(slot):
            if parent[slot] == slot:
                return slot
            parent[slot] = find(parent[slot])
            return parent[slot]
        
        def union(slot1, slot2):
            parent[find(slot1)] = find(slot2)
        
        max_profit = 0
        count_jobs = 0
        
        for p, d in jobs:
            available_slot = find(min(d, max_deadline))
            if available_slot > 0:
                union(available_slot, available_slot - 1)
                max_profit += p
                count_jobs += 1
        
        return [count_jobs, max_profit]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        deadline = list(map(int, input().strip().split()))
        profit = list(map(int, input().strip().split()))

        obj = Solution()
        ans = obj.jobSequencing(deadline, profit)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends
