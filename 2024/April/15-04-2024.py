#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here'
        nax = max(a)
        mp = [0] * (nax + 1)
        for i in b:
            if i <= nax:
                mp[i] += 1

        for i in range(1, nax + 1):
            mp[i] += mp[i - 1]

        out = []
        for i in query:
            out.append(mp[a[i]])

        return out
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends
