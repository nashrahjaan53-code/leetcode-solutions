class Solution:
    def minOperations(self, s1, s2):
        n = len(s1)
        if n == 1:
            if s1 == s2:
                return 0
            return 1 if s1[0] == '0' else -1
        
        # dp[i] = min ops to make s1[i:] == s2[i:]
        INF = 10**9
        dp = [INF] * (n + 1)
        dp[n] = 0
        
        def cost_pair(a, b):
            # Precomputed costs for all 4x4 possibilities
            if a == "11" and b == "00": return 1
            if a == "00" and b == "10": return 1
            if a == "00" and b == "01": return 1
            if a == "10" and b == "11": return 1
            if a == "01" and b == "11": return 1
            if a == "11" and b == "01": return 2
            if a == "11" and b == "10": return 2
            if a == "00" and b == "11": return 2
            if a == "10" and b == "00": return 2
            if a == "01" and b == "00": return 2
            if a == "01" and b == "10": return 3
            if a == "10" and b == "01": return 3
            return 0 if a == b else INF
        
        for i in range(n - 1, -1, -1):
            # Option 1: Handle single position i
            if s1[i] == s2[i]:
                dp[i] = dp[i + 1]
            else:
                if s1[i] == '0':
                    # Can turn 0->1 directly (1 op)
                    dp[i] = 1 + dp[i + 1]
                else:
                    # Need to "remove" this 1, which requires pairing with another 1 (costs 2 total for this pair effectively)
                    dp[i] = 2 + dp[i + 1]
            
            # Option 2: Handle pair (i, i+1) if possible
            if i + 1 < n:
                pair_cost = cost_pair(s1[i:i+2], s2[i:i+2])
                if pair_cost < INF:
                    dp[i] = min(dp[i], pair_cost + dp[i + 2])
        
        ans = dp[0]
        return ans if ans < INF else -1






        