#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        freq = {}
        
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        if len(set(freq.values())) == 1:
            return True
        
        if len(set(freq.values())) > 2:
            return False
        
        max_freq = max(freq.values())
        min_freq = min(freq.values())
        if list(freq.values()).count(max_freq) == 1 and max_freq - min_freq == 1:
            return True
        if list(freq.values()).count(min_freq) == 1 and min_freq == 1:
            return True
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends
