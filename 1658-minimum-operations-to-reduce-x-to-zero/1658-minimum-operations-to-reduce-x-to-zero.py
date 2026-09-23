class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        n = len(nums)
        max_len = -1
        current = 0
        left = 0
        for right in range(n):
            current += nums[right]
            while current > target and left <= right:
                current -= nums[left]
                left += 1
            if current == target:
                max_len = max(max_len, right - left + 1)
        return n - max_len if max_len != -1 else -1