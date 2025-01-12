#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        last_index = {}
        
        start = 0
        
        max_length = 0

        for i, char in enumerate(s):
            if char in last_index and last_index[char] >= start:
                start = last_index[char] + 1

            last_index[char] = i

            max_length = max(max_length, i - start + 1)

        return max_length

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends
