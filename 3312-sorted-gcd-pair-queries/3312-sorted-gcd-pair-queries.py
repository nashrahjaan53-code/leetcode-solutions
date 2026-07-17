class Solution(object):
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
        cnt_div = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            for multiple in range(d, max_val + 1, d):
                cnt_div[d] += freq[multiple]
        pairs_div = [0] * (max_val + 1)
        for d in range(1, max_val + 1):
            k = cnt_div[d]
            pairs_div[d] = k * (k - 1) // 2
        gcd_count = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            gcd_count[g] = pairs_div[g]
            for multiple in range(2 * g, max_val + 1, g):
                gcd_count[g] -= gcd_count[multiple]
        prefix = [0]
        for g in range(1, max_val + 1):
            if gcd_count[g] > 0:
                prefix.append(prefix[-1] + gcd_count[g])
        gcd_vals = [g for g in range(1, max_val + 1) if gcd_count[g] > 0]
        result = []
        for q in queries:

            left, right = 0, len(prefix) - 1
            while left < right:
                mid = (left + right) // 2
                if prefix[mid] <= q:
                    left = mid + 1
                else:
                    right = mid
            result.append(gcd_vals[left - 1])
        
        return result









 
        


        





        