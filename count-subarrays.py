class Solution:
    def countSubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        
        # Check every subarray
        for i in range(n):
            target_count = 0
            for j in range(i, n):
                # Count occurrences of target in current subarray
                if nums[j] == target:
                    target_count += 1
                
                # Length of current subarray
                length = j - i + 1
                
                # Check if target appears more than half
                if target_count > length / 2:
                    count += 1
        
        return count