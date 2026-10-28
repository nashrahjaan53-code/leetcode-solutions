class Solution:
    def createGrid(self, m, n):
        grid = [['#'] * n for _ in range(m)]
        # Create a single path: right along first row, then down the last column
        for j in range(n):
            grid[0][j] = '.'
        for i in range(m):
            grid[i][n-1] = '.'
        return [''.join(row) for row in grid]






        