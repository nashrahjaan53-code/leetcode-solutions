class Solution:
    def minScore(self, n, roads):

        graph = [[] for _ in range(n + 1)]
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        

        visited = set()
        
        def dfs(node):
            visited.add(node)
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(1)
        

        min_score = float('inf')
        for u, v, dist in roads:
            if u in visited or v in visited:
                min_score = min(min_score, dist)
        
        return min_score






        