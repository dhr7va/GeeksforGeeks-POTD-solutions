#User function Template for python3

class Solution:
    def pairAndSum(self, n, arr):
        #code here
        out = 0
        for i in range(32):
            cnt = 0
            for num in arr:
                if num & (1 << i):
                    cnt += 1
            pairs = (cnt * (cnt - 1) // 2)
            out += pairs * (1 << i)
        return out

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
# } Driver Code Ends
