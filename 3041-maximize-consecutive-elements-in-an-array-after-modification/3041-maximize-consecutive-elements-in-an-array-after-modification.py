class Solution:
    def maxSelectedElements(self, nums):
        nums.sort()
        result = 1
        dp = [1, 1]  # dp[0]: ending with x, dp[1]: ending with x+1, x = last value
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dp[1] = dp[0] + 1
            elif nums[i] == nums[i - 1] + 1:
                dp[0] += 1
                dp[1] += 1
            elif nums[i] == nums[i - 1] + 2:
                dp[0] = dp[1] + 1
                dp[1] = 1
            else:
                dp[0] = dp[1] = 1
            result = max(result, dp[0], dp[1])
        return result





        