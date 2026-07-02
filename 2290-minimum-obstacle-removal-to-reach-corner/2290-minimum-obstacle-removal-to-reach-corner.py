from collections import deque

class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        

        obstacles = [[float('inf')] * n for _ in range(m)]
        obstacles[0][0] = 0
        

        queue = deque([(0, 0, 0)])
        
        while queue:
            row, col, removed = queue.popleft()
            

            if row == m - 1 and col == n - 1:
                return removed
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_removed = removed + grid[new_row][new_col]
                    

                    if new_removed < obstacles[new_row][new_col]:
                        obstacles[new_row][new_col] = new_removed
                        
                        if grid[new_row][new_col] == 0:
                            queue.appendleft((new_row, new_col, new_removed))
                        else:
                            queue.append((new_row, new_col, new_removed))
        
        return obstacles[m-1][n-1]





        