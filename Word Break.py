#User function Template for python3

class Solution:
    def wordBreak(self, n, s, dictionary):

        word_set = set(dictionary)
        
        memo = {}
        
        def word_break_helper(s):
            if not s:
                return True
            
            if s in memo:
                return memo[s]
            
            for i in range(1, len(s) + 1):
                if s[:i] in word_set and word_break_helper(s[i:]):
                    memo[s] = True
                    return True
            
            memo[s] = False
            return False
        
        return word_break_helper(s)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends
