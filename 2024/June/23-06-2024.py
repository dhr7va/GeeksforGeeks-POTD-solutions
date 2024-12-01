#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
		# code here
        result = []
        stack = []
        counter = 0
        
        for char in str:
            if char == '(':
                counter += 1
                stack.append(counter)
                result.append(counter)
            elif char == ')':
                result.append(stack.pop())
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends
