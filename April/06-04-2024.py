#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        # code here
        n = len(arr)
        arr.sort() 
        res = []   
        
        for i in range(n - 3): 
            if i > 0 and arr[i] == arr[i - 1]: 
                continue
            
            for j in range(i + 1, n - 2): 
                if j > i + 1 and arr[j] == arr[j - 1]:  
                    continue
                
                left = j + 1 
                right = n - 1
                
                while left < right: 
                    curr_sum = arr[i] + arr[j] + arr[left] + arr[right]
                    
                    if curr_sum == k:
                        res.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        right -= 1
                        
                        while left < right and arr[left] == arr[left - 1]:
                            left += 1
                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1
                    elif curr_sum < k:
                        left += 1
                    else:
                        right -= 1
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends
