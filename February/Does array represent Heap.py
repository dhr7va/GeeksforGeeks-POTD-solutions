
class Solution:
    def isMaxHeap(self, arr, n):
        start = n // 2 - 1
        
        for i in range(start, -1, -1):
            if self.notMaxHeapify(arr, n, i):
                return False
        return True
    
    def notMaxHeapify(self, arr, n, i):
        left = 2 * i + 1
        right = 2 * i + 2
        
        largest = i
        
        if left < n and arr[left] > arr[largest]:
            largest = left
            
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            return True
        
        return False


#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends
