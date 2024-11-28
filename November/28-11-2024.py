#User function template for Python
class Solution:
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        s = s.lstrip()
        if not s:  
            return 0
        
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
        
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            index += 1
        
        result *= sign
        
        return result


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends
