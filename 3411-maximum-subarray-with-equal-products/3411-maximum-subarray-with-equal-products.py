class Solution:
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(nums)
        ans = 1
        for i in range(n):
            g = nums[i]
            l = nums[i]
            p = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                l = l * nums[j] // gcd(l, nums[j])
                p *= nums[j]
                if p == g * l:
                    ans = max(ans, j - i + 1)
                if p > 10**18:
                    break
        return ans





        