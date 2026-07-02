from collections import deque

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        

        min_cost = [[float('inf')] * n for _ in range(m)]
        

        queue = deque()
        
        start_cost = grid[0][0]
        if start_cost >= health:
            return False
        
        queue.append((0, 0, start_cost))
        min_cost[0][0] = start_cost
        
        while queue:
            row, col, cost = queue.popleft()
            

            if row == m - 1 and col == n - 1 and cost < health:
                return True
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_cost = cost + grid[new_row][new_col]
                    
                    # Only explore if path is better and health stays positive
                    if new_cost < min_cost[new_row][new_col] and new_cost < health:
                        min_cost[new_row][new_col] = new_cost
                        
                        # 0-1 BFS: push to left if cell is 0, right if cell is 1
                        if grid[new_row][new_col] == 0:
                            queue.appendleft((new_row, new_col, new_cost))
                        else:
                            queue.append((new_row, new_col, new_cost))
        
        return False






        