from collections import deque

class Solution:
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])
        

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        

        visited = set()
        visited.add((0, 0, 0))
        

        queue = deque([(0, 0, 0, 0)])
        
        while queue:
            row, col, eliminated, steps = queue.popleft()
            

            if row == m - 1 and col == n - 1:
                return steps
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_eliminated = eliminated + grid[new_row][new_col]
                    

                    if new_eliminated <= k and (new_row, new_col, new_eliminated) not in visited:
                        visited.add((new_row, new_col, new_eliminated))
                        queue.append((new_row, new_col, new_eliminated, steps + 1))
        
        return -1






        