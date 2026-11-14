class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        min_sum = float('inf')
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                length = j - i + 1
                if l <= length <= r and s > 0:
                    min_sum = min(min_sum, s)
        return min_sum if min_sum != float('inf') else -1
 






        