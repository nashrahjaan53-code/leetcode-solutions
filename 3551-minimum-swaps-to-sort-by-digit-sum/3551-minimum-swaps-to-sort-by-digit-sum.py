class Solution:
    def minSwaps(self, nums):
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        n = len(nums)
        indexed = [(digit_sum(nums[i]), nums[i], i) for i in range(n)]
        indexed.sort()
        pos = [0] * n
        for new_pos,(_, _, old_idx) in enumerate(indexed):
            pos[old_idx] = new_pos
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = pos[j]
        return n - cycles