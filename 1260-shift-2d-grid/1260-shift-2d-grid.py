class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        flat = sum(grid, [])
        k = k % (m * n)
        flat = flat[-k:] + flat[:-k] if k else flat
        return [flat[i*n:(i+1)*n] for i in range(m)]





