#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        
        n, m = len(arr1), len(arr2)
        
        low, high = max(0, k - m), min(k, n)
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = k - partition1
            
            maxLeft1 = float('-inf') if partition1 == 0 else arr1[partition1 - 1]
            minRight1 = float('inf') if partition1 == n else arr1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else arr2[partition2 - 1]
            minRight2 = float('inf') if partition2 == m else arr2[partition2]
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1
        
        return -1 
        
        


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
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
