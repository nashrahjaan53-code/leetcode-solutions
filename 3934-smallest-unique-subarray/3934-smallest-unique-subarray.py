class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        # Rolling hash parameters
        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9
        BASE1 = 911
        BASE2 = 3571
        
        # Precompute powers
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i-1] * BASE1) % MOD1
            pow2[i] = (pow2[i-1] * BASE2) % MOD2
        
        # Prefix hashes
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        for i in range(n):
            h1[i+1] = (h1[i] * BASE1 + nums[i]) % MOD1
            h2[i+1] = (h2[i] * BASE2 + nums[i]) % MOD2
        
        def get_hash(l, r):
            # hash of nums[l:r]
            x1 = (h1[r] - h1[l] * pow1[r-l] % MOD1 + MOD1) % MOD1
            x2 = (h2[r] - h2[l] * pow2[r-l] % MOD2 + MOD2) % MOD2
            return (x1, x2)
        
        def check(length):
            if length == 0:
                return False
            freq = {}
            for i in range(n - length + 1):
                h = get_hash(i, i + length)
                if h in freq:
                    freq[h] += 1
                else:
                    freq[h] = 1
            for v in freq.values():
                if v == 1:
                    return True
            return False
        
        # Binary search the minimal length
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo





        