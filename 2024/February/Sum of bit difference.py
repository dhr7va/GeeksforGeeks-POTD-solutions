#User function Template for python3
class Solution:

	
	def sumBitDifferences(self,arr, n):
        total_bit_diff = 0

        for i in range(32):
            count_set_bits = 0
            for num in arr:
                if num & (1 << i):
                    count_set_bits += 1

            total_bit_diff += count_set_bits * (n - count_set_bits) * 2

        return total_bit_diff
#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
