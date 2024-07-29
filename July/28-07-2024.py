#User function Template for python3
class Solution:
	def removeDups(self, str):
		# code here
        seen = set()
        result = []
        for char in str:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends
