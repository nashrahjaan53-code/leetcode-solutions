class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):

        edgeList.sort(key=lambda x: x[2])
        

        indexed_queries = [(limit, p, q, i) for i, (p, q, limit) in enumerate(queries)]
        indexed_queries.sort()
        
        uf = UnionFind(n)
        result = [False] * len(queries)
        edge_idx = 0
        
        for limit, p, q, query_idx in indexed_queries:

            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                u, v, _ = edgeList[edge_idx]
                uf.union(u, v)
                edge_idx += 1
            
            result[query_idx] = uf.connected(p, q)
        
        return result







        