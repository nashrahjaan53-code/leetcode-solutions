class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        k = k1 + k2
        if k == 0:
            return sum(d * d for d in diffs)
        left, right = 0, max(diffs) if diffs else 0
        def can_reduce_to(max_d):
            need = 0
            for d in diffs:
                if d > max_d:
                    need += d - max_d
                    if need > k:
                        return False
            return need <= k
        while left < right:
            mid = (left + right) // 2
            if can_reduce_to(mid):
                right = mid
            else:
                left = mid + 1
        remaining_k = k
        for i in range(n):
            if diffs[i] > left:
                remaining_k -= diffs[i] - left
                diffs[i] = left
        if left > 0:
            can_reduce = min(remaining_k, sum(1 for d in diffs if d == left))    
            ans = 0
            reduced = 0
            for d in diffs:
                if d == left and reduced < can_reduce:
                    ans += (left - 1) * (left - 1)
                    reduced += 1
                else:
                    ans += d * d
            return ans
        else:
            return 0



        