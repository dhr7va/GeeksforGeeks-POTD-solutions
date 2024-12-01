class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        if not nums:
            return [-1]
        
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        result = []
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        if result:
            return sorted(result)
        else:
            return [-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends
