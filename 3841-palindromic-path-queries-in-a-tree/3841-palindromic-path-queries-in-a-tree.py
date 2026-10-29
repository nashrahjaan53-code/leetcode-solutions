class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = [0]
        up = [[-1] * 17 for _ in range(n)]
        def dfs(u, p):
            parent[u] = p
            up[u][0] = p
            for k in range(1, 17):
                if up[u][k-1] != -1:
                    up[u][k] = up[up[u][k-1]][k-1]
            tin[u] = timer[0]
            timer[0] += 1
            for v in g[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)
            tout[u] = timer[0] - 1
        dfs(0,-1)
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for k in range(16, -1, -1):
                if up[u][k] != -1 and depth[up[u][k]] >= depth[v]:
                    u = up[u][k]
            if u == v:
                return u
            for k in range(16, -1, -1):
                if up[u][k] != -1 and up[u][k] != up[v][k]:
                    u = up[u][k]
                    v = up[v][k]
            return parent[u]
        bit = [0] * (n + 2)
        
        def add(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i
        def prefix(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res
        def range_xor(l, r, val):
            add(l, val)
            add(r + 1, val)
        masks = [1 << (ord(c) - ord('a')) for c in s]
        for i in range(n):
            range_xor(tin[i], tout[i], masks[i])
        def get_path_xor(u, v):
            if u == v:
                return masks[u]
            l = lca(u, v)
            pu = prefix(tin[u])
            pv = prefix(tin[v])
            return pu ^ pv ^ masks[l]
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                old = masks[u]
                delta = old ^ new_mask
                masks[u] = new_mask
                range_xor(tin[u], tout[u], delta)
            else:
                u = int(parts[1])
                v = int(parts[2])
                xor_mask = get_path_xor(u, v)
                # Check at most 1 bit set
                ans.append(bin(xor_mask).count('1') <= 1)
        return ans