#User function Template for python3


class Solution:
    def firstElementKTime(self, n, k, a):
        f = [0] * 201
        
        for i in range(n):
            f[a[i]] += 1
            
            if f[a[i]] == k:
                return a[i]
        
        return -1
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(n, k, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
