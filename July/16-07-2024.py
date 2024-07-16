#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		# code here
        occurrence = 0
        for i in range(len(s)):
            if s[i] == ch:
                occurrence += 1
                if occurrence == count:
                    return s[i + 1:]
        return ""

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends
