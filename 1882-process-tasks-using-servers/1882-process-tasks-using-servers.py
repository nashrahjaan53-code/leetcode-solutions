class Solution:
    def assignTasks(self, servers, tasks):
        n = len(servers)
        m = len(tasks)
        
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
        
        free = []
        for i in range(n):
            heap_push(free, (servers[i], i))
        busy = []
        ans = [0] * m
        t = 0
        j = 0
        while j < m:
            while busy and busy[0][0] <= t:
                ft, w, i = heap_pop(busy)
                heap_push(free, (w, i))
            while j < m and free and j <= t:
                w, i = heap_pop(free)
                ans[j] = i
                heap_push(busy, (t + tasks[j], w, i))
                j += 1
            if j < m and not free:
                if busy:
                    t = busy[0][0]
                else:
                    t = j
            else:
                t += 1
        return ans






        