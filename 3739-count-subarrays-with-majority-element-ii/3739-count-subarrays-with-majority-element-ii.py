class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        prefix_sum = 0
        freq = {0:1}

        result = 0
        prefix_sums = [0]
        offset = n + 1
        size = 2 * n + 3
        bit = [0] * size

        def update(idx, val):
            idx += offset
            while idx < size:
                bit[idx] += val
                idx += idx & -idx
        def query(idx):
            idx += offset 
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & -idx
            return res

        update(0,1)

        prefix_sum = 0
        for  num in nums:
            if num == target:
                prefix_sum += 1
            else:
                prefix_sum -= 1
             
            result += query(prefix_sum - 1)
            update(prefix_sum, 1)
        
        return result

      




        