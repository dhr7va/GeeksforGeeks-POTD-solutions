#User function Template for python3
class Solution:
    def findUnion(self, arr1, arr2, n, m):
        i = 0
        j = 0
        
        union = []
        
        while i < n and j < m:
            if arr1[i] == arr2[j]:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            else:
                if not union or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1
        
        while i < n:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        
        while j < m:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
        
        return union



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends
