class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        max_val = max(nums)
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        

        dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        dp[0][0] = 1
        
        for num in nums:
            new_dp = [row[:] for row in dp]
            
            for g1 in range(max_val + 1):
                for g2 in range(max_val + 1):
                    if dp[g1][g2] == 0:
                        continue
                    
  
                    new_g1 = num if g1 == 0 else gcd(g1, num)
                    new_dp[new_g1][g2] = (new_dp[new_g1][g2] + dp[g1][g2]) % MOD
                    
     
                    new_g2 = num if g2 == 0 else gcd(g2, num)
                    new_dp[g1][new_g2] = (new_dp[g1][new_g2] + dp[g1][g2]) % MOD
            
            dp = new_dp
        
        result = 0
        for g in range(1, max_val + 1):
            result = (result + dp[g][g]) % MOD
        
        return result





        