class Solution:
    def subarrayXor(self, arr, k):
        # code here

        count = 0
        prefixXOR = 0
        freq = {0: 1}  
        
        for num in arr:
            prefixXOR ^= num  
            
            target = prefixXOR ^ k
            if target in freq:
                count += freq[target]
            
            freq[prefixXOR] = freq.get(prefixXOR, 0) + 1
        
        return count
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends
