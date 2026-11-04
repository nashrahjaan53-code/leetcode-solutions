
class Solution:
    def minOperations(self, nums, x,k):
        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        # Fenwick trees: frequency and sum
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)

        def update(tree, i, delta):
            while i <= m:
                tree[i] += delta
                i += i & -i

        def query(tree, i):
            res = 0
            while i > 0:
                res += tree[i]
                i -= i & -i
            return res

        # Find kth smallest element
        def kth(kth_val):
            idx = 0
            bit = 1 << (m.bit_length() - 1)

            while bit:
                nxt = idx + bit
                if nxt <= m and cnt[nxt] < kth_val:
                    idx = nxt
                    kth_val -= cnt[nxt]
                bit >>= 1

            return idx + 1

        # Build first window
        window_sum = 0

        for i in range(x):
            v = nums[i]
            r = rank[v]
            update(cnt, r, 1)
            update(sm, r, v)
            window_sum += v

        costs = []

        # Calculate minimum cost for every window
        for start in range(n - x + 1):

            # Median
            mid = kth((x + 1) // 2)
            median = vals[mid - 1]

            # Values smaller than median
            left_count = query(cnt, mid - 1)
            left_sum = query(sm, mid - 1)

            # Values greater than or equal to median
            right_count = x - left_count
            right_sum = window_sum - left_sum

            # Minimum operations
            cost = (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

            costs.append(cost)

            # Slide window
            if start < n - x:
                old = nums[start]
                new = nums[start + x]

                update(cnt, rank[old], -1)
                update(sm, rank[old], -old)
                window_sum -= old

                update(cnt, rank[new], 1)
                update(sm, rank[new], new)
                window_sum += new

        # Dynamic Programming
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # Skip current element
                curr[i] = curr[i - 1]

                # Take a window of size x
                if i >= x:
                    candidate = prev[i - x] + costs[i - x]
                    curr[i] = min(curr[i], candidate)

            prev = curr

        return prev[n]








        