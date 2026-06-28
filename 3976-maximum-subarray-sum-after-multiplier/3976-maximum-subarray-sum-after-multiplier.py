class Solution:
    def maxSubarraySum(self, nums, k):
        def solve(transform):
            NEG = -10 ** 30
            dp0 = NEG
            dp1 = NEG
            dp2 = NEG
            ans = NEG

            for x in nums:
                y = transform(x)

                ndp0 = max(dp0 + x, x)
                ndp1 = max(
                    y,
                    dp0 + y,
                    dp1 + y
                )
                ndp2 = max(
                    dp2 + x,
                    dp1 + x
                )

                dp0, dp1, dp2 = ndp0, ndp1, ndp2
                ans = max(ans, dp0, dp1, dp2)

            return ans

        def divide(x):
            if x >= 0:
                return x // k
            return -((-x) // k)

        return max(
            solve(lambda x: x * k),
            solve(divide)
        )

    




        