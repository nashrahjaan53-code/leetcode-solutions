class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        def resolve(i, j, di, dj):
            while 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                if di == 0 and dj == 1:  # right -> down
                    di, dj = 1, 0
                    i += 1
                else:  # down -> right
                    di, dj = 0, 1
                    j += 1
            if 0 <= i < m and 0 <= j < n:
                return (i, j)
            return None
        
        memo = {}
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            res = 0
            # right
            nxt = resolve(i, j + 1, 0, 1)
            if nxt:
                res = (res + dfs(*nxt)) % MOD
            # down
            nxt = resolve(i + 1, j, 1, 0)
            if nxt:
                res = (res + dfs(*nxt)) % MOD
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)





