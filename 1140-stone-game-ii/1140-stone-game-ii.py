class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + piles[i]
        memo = [[-1] * (n + 1) for _ in range(n)]
        def dfs(i, m):
            if memo[i][m] != -1:
                return memo[i][m]
            if 2 * m >= n -i:
                memo[i][m] = s[n] - s[i]
                return memo[i][m]
            best = 0
            for x in range(1, 2 * m + 1):
                best = max(best, s[n] - s[i] - dfs(i+ x, max(m, x)))
            memo[i][m] = best
            return best
        return dfs(0, 1)
            

 



