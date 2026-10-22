class Solution:
    def minOperations(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        zero = nums.index(0)
        is_inc = True
        for i in range(n):
            if nums[(zero + i) % n] != i:
                is_inc = False
                break
        is_dec = True
        for i in range(n):
            if nums[(zero + i) % n] != (n - i) % n:
                is_dec = False
                break
        if not is_inc and not is_dec:
            return -1
        ans = float('inf')
        if is_inc:
            ans = min(ans, zero) 
            ans = min(ans, 2 + (n - zero) % n)
        if is_dec:
            ans  = min(ans,(zero + 1) % n + 1)
            ans = min(ans, 1 +(n - zero - 1) % n)
        return ans if ans != float('inf') else -1