#User function Template for python3

def max_sum(a,n):
    #code here
    total_sum = sum(a)
    
    curr_val = sum(i * a[i] for i in range(n))
    
    max_val = curr_val
    
    for i in range(1, n):
        curr_val = curr_val + total_sum - n * a[n - i]
        max_val = max(max_val, curr_val)
    
    return max_val

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends
