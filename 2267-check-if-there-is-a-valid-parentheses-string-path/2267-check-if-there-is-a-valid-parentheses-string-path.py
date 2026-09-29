class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        dp = [[set() for _ in range(n)] for _ in range(m)]
        start_bal = 1 if grid[0][0] == '(' else -1
        if start_bal < 0:
            return False
        dp[0][0].add(start_bal)
        
        for i in range(m):
            for j in range(n):
                if not dp[i][j]:
                    continue
                for bal in dp[i][j]:
                    # Move right
                    if j + 1 < n:
                        d = 1 if grid[i][j+1] == '(' else -1
                        new_bal = bal + d
                        rem = (m - i) + (n - j - 1) - 1
                        if new_bal >= 0 and new_bal <= rem:
                            dp[i][j+1].add(new_bal)
                    if i + 1 < m:
                        d = 1 if grid[i+1][j] == '(' else -1
                        new_bal = bal + d
                        rem = (m - i - 1) + (n - j) - 1
                        if new_bal >= 0 and new_bal <= rem:
                            dp[i+1][j].add(new_bal)
        return 0 in dp[m-1][n-1]