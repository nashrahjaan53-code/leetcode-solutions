class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        cost = [[float('inf')] * (n + 1) for _ in range(n)]
        for i in range(n):
            for j in range(i + 2, n + 1):
                L = j - i
                min_c = float('inf')
                for d in range(1, L):
                    if L % d == 0:
                        c = 0
                        for g in range(d):
                            group = [s[p] for p in range(i + g, j, d)]
                            m = len(group)
                            for t in range(m // 2):
                                if group[t] != group[m - 1 - t]:
                                    c += 1
                        if c < min_c:
                            min_c = c
                cost[i][j] = min_c
        
        INF = 10**9
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for q in range(1, k + 1):
            for p in range(2 * q, n + 1):
                for prev in range(p - 2, 2 * (q - 1) - 1, -1):
                    if prev >= 0:
                        dp[p][q] = min(dp[p][q], dp[prev][q - 1] + cost[prev][p])
        return dp[n][k]






        