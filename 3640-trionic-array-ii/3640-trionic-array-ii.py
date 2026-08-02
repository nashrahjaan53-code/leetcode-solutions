class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)
        NEG_INF = float('-inf')
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        maxleft = [NEG_INF] * n   
        maxright = [NEG_INF] * n  


        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] > nums[j]:
                j += 1

            if j > i:

                cur_min = prefix[i]
                for p in range(i + 1, j + 1):
                    maxleft[p] = prefix[p] - cur_min
                    cur_min = min(cur_min, prefix[p])

                cur_max = prefix[j + 1]
                for q in range(j - 1, i - 1, -1):
                    maxright[q] = cur_max - prefix[q + 1]
                    cur_max = max(cur_max, prefix[q + 1])
            i = j + 1

        ans = NEG_INF


        i = 0
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] < nums[j]:
                j += 1

            if j > i:
                run_max_A = NEG_INF         
                for q in range(i + 1, j + 1):
                    p = q - 1
                    if maxleft[p] > NEG_INF:
                        A = maxleft[p] - prefix[p]
                        run_max_A = max(run_max_A, A)
                    if maxright[q] > NEG_INF and run_max_A > NEG_INF:
                        B = prefix[q + 1] + maxright[q]
                        ans = max(ans, run_max_A + B)
            i = j + 1

        return ans





        