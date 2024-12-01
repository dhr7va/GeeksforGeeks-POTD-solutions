#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        cumulative_sum_count = {}
        
        cumulative_sum = 0
        count = 0
        
        cumulative_sum_count[0] = 1
        
        for num in arr:
            cumulative_sum += num
            
            if cumulative_sum - tar in cumulative_sum_count:
                count += cumulative_sum_count[cumulative_sum - tar]
            
            if cumulative_sum in cumulative_sum_count:
                cumulative_sum_count[cumulative_sum] += 1
            else:
                cumulative_sum_count[cumulative_sum] = 1
        
        return count

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends
