class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        min_idx = 0
        max_idx = 0
        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)
        opt1 = b + 1
        opt2 = n - a
        opt3 = (a + 1) + (n - b)
        return min(opt1, opt2, opt3)




        