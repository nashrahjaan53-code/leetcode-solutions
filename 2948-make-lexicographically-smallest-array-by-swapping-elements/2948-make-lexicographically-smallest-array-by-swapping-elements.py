class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        arr = sorted((val, idx) for idx, val in enumerate(nums))
        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1
            indices = sorted(idx for _, idx in arr[i:j])
            values = [val for val, _ in arr[i:j]]
            for k, val in zip(indices, values):
                ans[k] = val
            i = j
        return ans
               






        