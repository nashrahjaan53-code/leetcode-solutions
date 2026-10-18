class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        N = 1001
        fact = [1] * N
        invfact = [1] * N
        for i in range(1,N):
            fact[i] = fact[i-1] * i % MOD
        invfact[N-1] = pow(fact[N-1],MOD-2,MOD)
        for i in range(N-2, -1, -1):
            invfact[i] = invfact[i+1] * (i+1) % MOD
        def comb(n,k):
            if k < 0 or k > n:
                return 0
            return fact[n] * invfact[k] % MOD * invfact[n-k] % MOD
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            ways_left = dfs(left)
            ways_right = dfs(right)
            return comb(len(left) + len(right), len(left)) * ways_left % MOD * ways_right % MOD
        return (dfs(nums) - 1) % MOD