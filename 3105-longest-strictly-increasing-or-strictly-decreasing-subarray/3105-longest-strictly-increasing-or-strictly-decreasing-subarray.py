class Solution:
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        max_len = 1
        # Check increasing
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    max_len = max(max_len, j - i + 1)
                else:
                    break
        # Check decreasing
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] < nums[j - 1]:
                    max_len = max(max_len, j - i + 1)
                else:
                    break
        return max_len





        