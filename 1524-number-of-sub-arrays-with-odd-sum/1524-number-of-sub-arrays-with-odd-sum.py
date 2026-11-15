class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        even = 1  # empty prefix even
        odd = 0
        ans = 0
        prefix = 0
        for x in arr:
            prefix += x
            if prefix % 2 == 0:
                ans = (ans + odd) % MOD
                even += 1
            else:
                ans = (ans + even) % MOD
                odd += 1
        return ans

        


       
        