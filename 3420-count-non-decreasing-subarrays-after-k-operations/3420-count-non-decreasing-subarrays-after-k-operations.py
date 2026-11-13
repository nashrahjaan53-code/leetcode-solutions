class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        ans = 0
        cost = 0
        dq = []  # list as deque, append right, pop(0) left
        j = n - 1
        for i in range(n - 1, -1, -1):
            count = 1
            while dq and dq[-1][0] < nums[i]:
                nextNum, nextCount = dq.pop()
                count += nextCount
                cost += (nums[i] - nextNum) * nextCount
            dq.append((nums[i], count))
            while cost > k:
                rightmostNum, rightmostCount = dq.pop(0)
                cost -= (rightmostNum - nums[j])
                j -= 1
                if rightmostCount > 1:
                    dq.insert(0, (rightmostNum, rightmostCount - 1))
            ans += j - i + 1
        return ans






        