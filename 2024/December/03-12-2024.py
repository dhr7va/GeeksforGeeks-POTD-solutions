class Solution:
    def minChar(self, s):
        #Write your code here
        rev_s = s[::-1]
        
        temp = s + '#' + rev_s
        
        n = len(temp)
        lps = [0] * n
        length = 0  
        for i in range(1, n):
            while length > 0 and temp[i] != temp[length]:
                length = lps[length - 1]
            if temp[i] == temp[length]:
                length += 1
            lps[i] = length
        
        return len(s) - lps[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends
