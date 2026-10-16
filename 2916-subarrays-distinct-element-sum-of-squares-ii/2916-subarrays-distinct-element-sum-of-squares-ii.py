class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        
        # Fenwick trees for range update + range sum (on the cnt values)
        # Use difference array style: bit1 for sum of values, bit2 for sum of (i+1)*values
        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)
        
        def add(bit, i, val):
            i += 1
            while i <= n + 1:
                bit[i] = (bit[i] + val) % MOD
                i += i & -i
        
        def prefix(bit, i):
            i += 1
            res = 0
            while i > 0:
                res = (res + bit[i]) % MOD
                i -= i & -i
            return res
        
        def range_add(l, r, val):
            # range add val to [l, r]
            add(bit1, l, val)
            add(bit1, r + 1, -val)
            add(bit2, l, val * l % MOD)
            add(bit2, r + 1, -val * (r + 1) % MOD)
        
        def range_sum(l, r):
            # sum of cnt[l..r]
            def pref(x):
                if x < 0:
                    return 0
                return (prefix(bit1, x) * (x + 1) - prefix(bit2, x)) % MOD
            return (pref(r) - pref(l - 1)) % MOD
        
        last = {}
        ans = 0
        cur_sum = 0  # current sum of cnt for L=0 to current max
        cur_sum_sq = 0
        
        for r in range(n):
            x = nums[r]
            p = last.get(x, -1)
            # Add +1 to [p+1, r]
            if p + 1 <= r:
                # increase sum_sq by 2 * sum_[p+1,r] + length
                length = r - p
                s = range_sum(p + 1, r)
                cur_sum_sq = (cur_sum_sq + 2 * s + length) % MOD
                cur_sum = (cur_sum + length) % MOD
                range_add(p + 1, r, 1)
            ans = (ans + cur_sum_sq) % MOD
            last[x] = r
        
        return ans





        