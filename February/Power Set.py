class Solution:
    def __init__(self):
        self.ans = []

    def AllPossibleStrings(self, s):
        def sub(p, cur):
            if p == len(s):
                if cur:
                    self.ans.append(cur)
                return

            sub(p + 1, cur + s[p])  
            sub(p + 1, cur)         

        sub(0, "")
        self.ans.sort()
        return self.ans
#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends
