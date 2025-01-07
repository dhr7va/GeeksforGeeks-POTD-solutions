#User function Template for python3
class Solution:class Solution:


    def sumClosest(self, arr, target):
        # code here
        if len(arr) < 2:
            return []

        arr.sort()  
        left = 0
        right = len(arr) - 1
        closest_sum = float('inf')
        best_pair = []

        while left < right:
            current_sum = arr[left] + arr[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
                best_pair = [arr[left], arr[right]]
            elif abs(current_sum - target) == abs(closest_sum - target):
                if (arr[right] - arr[left]) > (best_pair[1] - best_pair[0]):
                    best_pair = [arr[left], arr[right]]
            
            if current_sum < target:
                left += 1
            else:
                right -= 1
        
        return best_pair


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
