class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        
        # New parent
        new_parent = parent[:]
        last = [-1] * 26  # last ancestor of each char
        
        def dfs(u):
            c = ord(s[u]) - ord('a')
            prev = last[c]
            if prev != -1:
                new_parent[u] = prev
            last[c] = u
            for v in children[u]:
                dfs(v)
            last[c] = prev
        
        dfs(0)
        
        # Build new children
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
        
        # Compute sizes
        size = [0] * n
        def dfs_size(u):
            size[u] = 1
            for v in new_children[u]:
                dfs_size(v)
                size[u] += size[v]
        
        dfs_size(0)
        return size
    





        