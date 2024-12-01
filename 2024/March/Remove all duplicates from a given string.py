#User function Template for python3
class Solution:

	
	def removeDuplicates(self,s):
	    # code here
        char_freq = {}
        
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        result = ""
        for char in s:
            if char_freq[char] > 0:
                result += char
                char_freq[char] = 0
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends
