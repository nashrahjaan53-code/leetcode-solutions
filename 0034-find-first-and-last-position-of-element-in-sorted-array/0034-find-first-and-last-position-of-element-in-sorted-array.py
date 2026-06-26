import bisect
class Solution:
    def searchRange(self, nums, target):
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1

        if left <= right:
            return [left, right]
        return [-1, -1]
      


      

        