class Solution:
    def findMissingElements(self, nums):
        nums.sort()
        missing = []
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                for num in range(nums[i] + 1, nums[i + 1]):
                    missing.append(num)
        return missing




        