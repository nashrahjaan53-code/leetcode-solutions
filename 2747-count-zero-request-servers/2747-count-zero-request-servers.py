class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda t: t[1])
        q_idx = sorted(range(len(queries)), key=lambda i: queries[i])
        ans = [0] * len(queries)
        cnt = [0] * (n + 1)
        active = 0
        left = 0
        right = 0
        m = len(logs)
        for qi in q_idx:
            q = queries[qi]
            L = q - x
            R = q
            while right < m and logs[right][1] <= R:
                s = logs[right][0]
                if cnt[s] == 0:
                    active += 1
                cnt[s] += 1
                right += 1
            while left < m and logs[left][1] < L:
                s = logs[left][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1
                left += 1
            ans[qi] = n - active
        return ans








        