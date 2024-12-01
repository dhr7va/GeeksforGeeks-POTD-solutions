#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        # code here
        result = [0] * n
        seen = set()
        result[0] = 0
        seen.add(0)
        
        for i in range(1, n):
            prev = result[i - 1]
            candidate1 = prev - i
            candidate2 = prev + i
            
            if candidate1 >= 0 and candidate1 not in seen:
                result[i] = candidate1
                seen.add(candidate1)
            else:
                result[i] = candidate2
                seen.add(candidate2)
        
        return result
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends
