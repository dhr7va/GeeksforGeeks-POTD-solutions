class Solution:
    def ExtractNumber(self,sentence):
        #code here
        words = sentence.split()
        
        numbers = [int(word) for word in words if word.isdigit() and '9' not in word]
        
        if not numbers:
            return -1
        
        return max(numbers)

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends
