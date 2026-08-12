class Solution:
    def maxSubarrayLength(self, nums, k):
        freq = {}
        left = 0
        max_len = 0
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0 ) + 1
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len

       





        