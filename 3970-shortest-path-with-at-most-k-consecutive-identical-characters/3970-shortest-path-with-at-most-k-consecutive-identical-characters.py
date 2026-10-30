class Solution:
    def shortestPath(self, n, edges, labels, k):
        g =[[] for _ in range(n)]
        for u,v,w in edges:
            g[u].append((v,w))
        INF = 10**18
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]
        
        def heap_push(item):
            heap.append(item)
            i = len(heap) - 1
            while i > 0:
                p = (i - 1) // 2
                if heap[p][0] <= heap[i][0]:
                    break
                heap[p], heap[i] = heap[i], heap[p]
                i = p
        
        def heap_pop():
            if not heap:
                return None
            res = heap[0]
            last = heap.pop()
            if heap:
                heap[0] = last
                i = 0
                while True:
                    l = 2 * i + 1
                    r = 2 * i + 2
                    smallest = i
                    if l < len(heap) and heap[l][0] < heap[smallest][0]:
                        smallest = l
                    if r < len(heap) and heap[r][0] < heap[smallest][0]:
                        smallest = r
                    if smallest == i:
                        break
                    heap[i], heap[smallest] = heap[smallest], heap[i]
                    i = smallest
            return res
        while heap:
            cost, u, consec = heap_pop()
            if cost > dist[u][consec]:
                continue
            if u == n - 1:
                return cost
            for v, w in g[u]:
                if labels[v] == labels[u]:
                    new_consec = consec + 1
                else:
                    new_consec = 1
                if new_consec > k:
                    continue
                new_cost = cost + w
                if new_cost < dist[v][new_consec]:
                    dist[v][new_consec] = new_cost
                    heap_push((new_cost, v, new_consec))
        return -1