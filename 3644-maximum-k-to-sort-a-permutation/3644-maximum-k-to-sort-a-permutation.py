class Solution:
    def sortPermutation(self, nums):
        res = -1
        for i, x in enumerate(nums):
            if x != i:
                if res == -1:
                    res = x
                else: 
                   res &= x
        return res if res != -1 else 0