class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        count = [0] * 51
        
        for i in range(n - k + 1):
            seen = set()
            for j in range(i, i + k):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    count[nums[j]] += 1
        
        for num in range(50, -1, -1):
            if count[num] == 1:
                return num
        
        return -1






       