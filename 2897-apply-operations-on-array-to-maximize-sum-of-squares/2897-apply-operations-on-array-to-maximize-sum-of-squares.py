class Solution:
    def maxSum(self, nums, k):
        MOD = 10 ** 9 + 7
        bit_count = [0] * 31
        for num in nums:
            for b in range(31):
                if num & (1 << b):
                    bit_count[b] += 1
        res_nums = [0] * k
        for b in range(30, -1, -1):
            cnt = min(bit_count[b], k)
            for i in range(cnt):
                res_nums[i] |= (1 << b)
        ans = 0
        for x in res_nums:
            ans = (ans + x * x) % MOD
        return ans