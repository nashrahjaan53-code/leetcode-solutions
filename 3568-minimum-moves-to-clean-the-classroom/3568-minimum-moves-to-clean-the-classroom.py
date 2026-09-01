


class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        grid = [list(row) for row in classroom]
        
        start = None
        litters = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    start = (i, j)
                elif grid[i][j] == 'L':
                    litters.append((i, j))
        
        L = len(litters)
        full_mask = (1 << L) - 1
        litter_id = {pos: idx for idx, pos in enumerate(litters)}
        

        visited = [[[-1] * (1 << L) for _ in range(n)] for _ in range(m)]
        
        q = []
        sr, sc = start
        q.append((sr, sc, 0, energy, 0)) 
        visited[sr][sc][0] = energy
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        head = 0
        
        while head < len(q):
            r, c, mask, e, steps = q[head]
            head += 1
            
            if mask == full_mask:
                return steps
            

            if e < visited[r][c][mask]:
                continue
            
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] == 'X':
                    continue
                
                ne = e - 1
                if ne < 0:
                    continue
                
                new_mask = mask
                cell = grid[nr][nc]
                
                if cell == 'L':
                    idx = litter_id.get((nr, nc))
                    if idx is not None:
                        new_mask |= (1 << idx)
                
                if cell == 'R':
                    ne = energy
                
                if ne > visited[nr][nc][new_mask]:
                    visited[nr][nc][new_mask] = ne
                    q.append((nr, nc, new_mask, ne, steps + 1))
        
        return -1







        