class Solution(object):
    def maxAlternatingSum(self, nums):
        squares = [x * x for x in nums]
        squares.sort()
        n = len(squares)
        ans = 0
        neg = n // 2
        for i in range(neg):
            ans -= squares[i]
        for i in range(neg, n):
            ans += squares[i]
        return ans