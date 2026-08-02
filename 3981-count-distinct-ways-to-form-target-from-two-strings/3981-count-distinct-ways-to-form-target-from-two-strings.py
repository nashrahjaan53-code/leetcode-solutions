class Solution:
    def interleaveCharacters(self, word1, word2, target):
        MOD = 10**9 + 7
        n1, n2, m = len(word1), len(word2), len(target)
        if m == 0:
            return 0


        dp = [[[0] * (n2 + 1) for _ in range(n1 + 1)] for _ in range(m + 1)]
        for i1 in range(n1 + 1):
            for i2 in range(n2 + 1):
                dp[m][i1][i2] = 1

        for k in range(m - 1, -1, -1):


            suffix1 = [[0] * (n1 + 1) for _ in range(n2 + 1)]
            for i2 in range(n2 + 1):
                s = 0
                for i1 in range(n1 - 1, -1, -1):
                    if word1[i1] == target[k]:
                        s = (s + dp[k + 1][i1 + 1][i2]) % MOD
                    suffix1[i2][i1] = s


            suffix2 = [[0] * (n2 + 1) for _ in range(n1 + 1)]
            for i1 in range(n1 + 1):
                s = 0
                for i2 in range(n2 - 1, -1, -1):
                    if word2[i2] == target[k]:
                        s = (s + dp[k + 1][i1][i2 + 1]) % MOD
                    suffix2[i1][i2] = s

            for i1 in range(n1 + 1):
                for i2 in range(n2 + 1):
                    dp[k][i1][i2] = (suffix1[i2][i1] + suffix2[i1][i2]) % MOD

        total = dp[0][0][0]


        def count_single(w, t):
            dps = [0] * (len(t) + 1)
            dps[0] = 1
            for ch in w:
                for j in range(len(t) - 1, -1, -1):
                    if ch == t[j]:
                        dps[j + 1] = (dps[j + 1] + dps[j]) % MOD
            return dps[-1]

        all1 = count_single(word1, target)
        all2 = count_single(word2, target)
        return (total - all1 - all2 + 2 * MOD) % MOD







        