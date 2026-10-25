class Solution:
    def closedIsland(self, grid):
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 0:
                return
            grid[i][j] = 1  
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # Flood fill all border 0s
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n-1] == 0:
                dfs(i, n-1)
        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m-1][j] == 0:
                dfs(m-1, j)
        
        # Count remaining islands
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count






        