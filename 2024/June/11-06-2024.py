
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        diffs = sorted([(abs(arr[i] - brr[i]), i) for i in range(n)], reverse=True)
        
        total_tips = 0
        a_orders = 0
        b_orders = 0
        
        for _, i in diffs:
            if (arr[i] > brr[i] and a_orders < x) or b_orders >= y:
                total_tips += arr[i]
                a_orders += 1
            else:
                total_tips += brr[i]
                b_orders += 1
        
        return total_tips      



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends
