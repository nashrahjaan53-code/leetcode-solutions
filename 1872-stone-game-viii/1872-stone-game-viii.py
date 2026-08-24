class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)
        for i in range(1,n):
            stones[i] += stones[i - 1]
        f = stones[-1]
        for i in range(n - 2, 0, -1):
            f = max(f, stones[i] - f)
        return f
 



        