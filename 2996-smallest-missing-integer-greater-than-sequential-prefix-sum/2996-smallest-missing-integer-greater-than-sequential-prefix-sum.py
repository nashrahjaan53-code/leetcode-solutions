class Solution:
    def missingInteger(self, nums):
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            i += 1
        s = sum(nums[:i])
        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x





        