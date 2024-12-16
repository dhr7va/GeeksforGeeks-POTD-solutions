#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        i, j = 0, 0
        
        while k > 1:
            if i < len(a) and (j >= len(b) or a[i] <= b[j]):
                i += 1
            else:
                j += 1
            k -= 1

        if i < len(a) and (j >= len(b) or a[i] <= b[j]):
            return a[i]
        else:
            return b[j]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
