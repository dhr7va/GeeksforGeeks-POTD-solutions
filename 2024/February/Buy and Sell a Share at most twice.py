from typing import List


class Solution:
    def maxProfit(self, n: int, price: List[int]) -> int:
        if n <= 1:
            return 0

        max_profit_one = [0] * n

        max_profit_two = [0] * n

        min_price = price[0]
        for i in range(1, n):
            min_price = min(min_price, price[i])
            max_profit_one[i] = max(max_profit_one[i - 1], price[i] - min_price)

        max_price = price[n - 1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, price[i])
            max_profit_two[i] = max(max_profit_two[i + 1], max_price - price[i])

        max_profit = max_profit_one[n - 1]
        for i in range(n - 1):
            max_profit = max(max_profit, max_profit_one[i] + max_profit_two[i + 1])

        return max_profit

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends
