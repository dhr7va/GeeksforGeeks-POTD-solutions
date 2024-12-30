#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
        seen = {}
        
        for i, num in enumerate(arr):
            complement = target - num
            
            if complement in seen:
                return True
            
            seen[num] = i
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
