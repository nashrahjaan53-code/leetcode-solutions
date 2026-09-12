class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        arr = sorted((intervals[i][0], intervals[i][1], intervals[i][2],i) for i in range(n))
        next_idx = [n] * n
        for i in range(n):
            lo, hi = i + 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid][0] > arr[i][1]:
                    hi = mid
                else:
                    lo = mid + 1
            next_idx[i] = lo
        memo = [[None] * 5 for _ in range(n + 1)]
        def dp(i,k):
            if i >= n or k == 0:
                return (0,())
            if memo[i][k] is not None:
                return memo[i][k]
            skip_w, skip_idx = dp(i + 1, k)
            take_w, take_idx = dp(next_idx[i], k -1)
            take_w += arr[i][2]
            take_idx = tuple(sorted((arr[i][3],) + take_idx))
            if take_w > skip_w or(take_w == skip_w and take_idx < skip_idx):
                res = (take_w, take_idx)
            else:
                res = (skip_w, skip_idx)
            memo[i][k] = res
            return res
        _, indices = dp(0, 4)
        return list(indices)













        