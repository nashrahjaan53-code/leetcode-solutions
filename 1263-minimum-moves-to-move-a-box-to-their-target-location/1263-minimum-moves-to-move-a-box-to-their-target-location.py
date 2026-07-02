from collections import deque

class Solution:
    def minPushBox(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        

        player = box = target = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)
        
        def can_reach(start, end, box_pos):

            if start == end:
                return True
            
            visited = set()
            queue = deque([start])
            visited.add(start)
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and 
                        grid[nr][nc] != '#' and 
                        (nr, nc) != box_pos and 
                        (nr, nc) not in visited):
                        if (nr, nc) == end:
                            return True
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False
        


        visited = set()
        queue = deque([(box[0], box[1], player[0], player[1], 0)])
        visited.add((box[0], box[1], player[0], player[1]))
        
        while queue:
            br, bc, pr, pc, pushes = queue.popleft()
            
            if (br, bc) == target:
                return pushes
            
            for dr, dc in directions:

                nbr, nbc = br + dr, bc + dc

                push_pos = (br - dr, bc - dc)
                
                if (0 <= nbr < m and 0 <= nbc < n and 
                    grid[nbr][nbc] != '#' and
                    0 <= push_pos[0] < m and 0 <= push_pos[1] < n and
                    grid[push_pos[0]][push_pos[1]] != '#' and
                    (nbr, nbc, br, bc) not in visited and
                    can_reach((pr, pc), push_pos, (br, bc))):
                    
                    visited.add((nbr, nbc, br, bc))
                    queue.append((nbr, nbc, br, bc, pushes + 1))
        
        return -1





        