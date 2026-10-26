class Solution:
    def countIslands(self, grid, k):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            total = grid[i][j]
            total += dfs(i+1, j)
            total += dfs(i-1, j)
            total += dfs(i, j+1)
            total +=dfs(i, j-1)
            return total
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0  and not visited[i][j]:
                    s = dfs(i,j)
                    if s % k == 0:
                        count += 1
        return count