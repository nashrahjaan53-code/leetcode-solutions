class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        last = [0] * 26
        total = 0
        for c in s:
            idx = ord(c) - ord('a')
            new =(total - last[idx] + 1) % MOD
            total = (total + new) % MOD
            last[idx] = (last[idx] + new) % MOD
        return total




        