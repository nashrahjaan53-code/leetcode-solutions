from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        

        graph = [[] for _ in range(n)]
        for u, v, cost in edges:
            graph[u].append((v, cost))
        

        costs = sorted(set(cost for _, _, cost in edges))
        
        def can_reach(min_score):


            dp = [float('inf')] * n
            dp[0] = 0
            

            indegree = [0] * n
            for u in range(n):
                for v, cost in graph[u]:
                    indegree[v] += 1
            
            queue = deque([i for i in range(n) if indegree[i] == 0])
            
            while queue:
                u = queue.popleft()
                
                if dp[u] != float('inf') and online[u]:
                    for v, cost in graph[u]:
                        if cost >= min_score and online[v]:
                            dp[v] = min(dp[v], dp[u] + cost)
                
                for v, _ in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            
            return dp[n-1] <= k
        

        left, right = 0, len(costs) - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_reach(costs[mid]):
                ans = costs[mid]
                left = mid + 1
            else:
                right = mid - 1
        
        return ans







