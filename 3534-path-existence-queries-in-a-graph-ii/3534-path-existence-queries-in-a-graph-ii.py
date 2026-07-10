import sys

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # 1. sort node indices by value
        sorted_idx = sorted(range(n), key=lambda i: nums[i])
        sorted_vals = [nums[i] for i in sorted_idx]

        # 2. two-pointer: far[i] = farthest position reachable in 1 hop from sorted position i
        far = [0] * n
        right = 0
        for i in range(n):
            if right < i:
                right = i
            while right + 1 < n and sorted_vals[right + 1] - sorted_vals[i] <= maxDiff:
                right += 1
            far[i] = right

        # 3. rank[original_index] = position in sorted order
        rank = [0] * n
        for pos, idx in enumerate(sorted_idx):
            rank[idx] = pos

        # 4. binary lifting table
        LOG = 1
        while (1 << LOG) < n:
            LOG += 1
        LOG += 1

        jump = [far[:]]
        for k in range(1, LOG):
            prev = jump[-1]
            jump.append([prev[prev[i]] for i in range(n)])

        ans = []
        for u, v in queries:
            p, q = rank[u], rank[v]
            if p > q:
                p, q = q, p
            if p == q:
                ans.append(0)
                continue

            cur, steps = p, 0
            for k in range(LOG - 1, -1, -1):
                nxt = jump[k][cur]
                if nxt < q:
                    cur = nxt
                    steps += (1 << k)

            if far[cur] >= q:
                ans.append(steps + 1)
            else:
                ans.append(-1)

        return ans

        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        