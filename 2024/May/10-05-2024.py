#User function Template for python3
class Solution:
    
    def CombinationSum2(self, arr, n, k):
        result = []
        
        def find_combinations(index, current_sum, current_combination):
            if current_sum == k:
                result.append(list(current_combination))
                return
            
            if current_sum > k:
                return
            
            for i in range(index, n):
                if i > index and arr[i] == arr[i - 1]:
                    continue
                
                current_combination.append(arr[i])
                find_combinations(i + 1, current_sum + arr[i], current_combination)
                current_combination.pop()
        
        arr.sort()
        
        find_combinations(0, 0, [])
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)
    for row in result:
        print(*row)
    if not result:
        print()

# } Driver Code Ends
