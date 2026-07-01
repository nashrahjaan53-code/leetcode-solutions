import heapq

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        

        dist = [[float('inf')] * n for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        


        max_heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while max_heap:
            safeness, r, c = heapq.heappop(max_heap)
            safeness = -safeness
            
            if r == n-1 and c == n-1:
                return safeness
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    new_safeness = min(safeness, dist[nr][nc])
                    heapq.heappush(max_heap, (-new_safeness, nr, nc))
        
        return 0





        