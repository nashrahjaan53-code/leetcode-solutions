class Solution:
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = float('inf')
            for j in range(1, 4):
                if i - j >= 0:
                    cost = costs[i - 1] + (j * j)
                    dp[i] = min(dp[i], dp[i - j] + cost)
        return dp[n]