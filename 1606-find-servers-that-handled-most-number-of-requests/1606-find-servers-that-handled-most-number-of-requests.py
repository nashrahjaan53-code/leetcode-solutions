class Solution:
    def busiestServers(self, k, arrival, load):
        m = len(arrival)
        count = [0] * k
        free = list(range(k))
        busy = []
        
        def heap_push(heap, item):
            heap.append(item)
            i = len(heap) - 1
            while i > 0:
                p = (i - 1) // 2
                if heap[p] <= heap[i]:
                    break
                heap[p], heap[i] = heap[i], heap[p]
                i = p
        
        def heap_pop(heap):
            if not heap:
                return None
            res = heap[0]
            last = heap.pop()
            if heap:
                heap[0] = last
                i = 0
                n = len(heap)
                while True:
                    l = 2 * i + 1
                    r = 2 * i + 2
                    smallest = i
                    if l < n and heap[l] < heap[smallest]:
                        smallest = l
                    if r < n and heap[r] < heap[smallest]:
                        smallest = r
                    if smallest == i:
                        break
                    heap[i], heap[smallest] = heap[smallest], heap[i]
                    i = smallest
            return res
        
        for i in range(m):
            t = arrival[i]
            while busy and busy[0][0] <= t:
                ft, s = heap_pop(busy)
                # insert s into free sorted
                lo, hi = 0, len(free)
                while lo < hi:
                    mid = (lo + hi) // 2
                    if free[mid] < s:
                        lo = mid + 1
                    else:
                        hi = mid
                free.insert(lo, s)
            if not free:
                continue
            target = i % k
            lo, hi = 0, len(free)
            while lo < hi:
                mid = (lo + hi) // 2
                if free[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            if lo < len(free):
                s = free.pop(lo)
            else:
                s = free.pop(0)
            count[s] += 1
            heap_push(busy, (t + load[i], s))
        
        max_c = max(count)
        return [i for i in range(k) if count[i] == max_c]




 


        