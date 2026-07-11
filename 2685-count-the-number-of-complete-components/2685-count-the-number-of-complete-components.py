class Solution:
    def countCompleteComponents(self, n, edges):
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        result = 0
        
        for i in range(n):
            if not visited[i]:
                # Find all vertices in this component
                component = []
                stack = [i]
                visited[i] = True
                
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                
                # Check if component is complete
                k = len(component)
                is_complete = True
                
                # Check every pair in component has an edge
                for a in range(k):
                    for b in range(a + 1, k):
                        # Check if edge exists between component[a] and component[b]
                        if component[b] not in adj[component[a]]:
                            is_complete = False
                            break
                    if not is_complete:
                        break
                
                if is_complete:
                    result += 1
        
        return result

        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        