class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            current_sum = 0
            for j in range(1, 4):
                if i + j - 1 < n:
                    current_sum += stoneValue[i + j - 1]
                    best = max(best, current_sum - dp[i + j])
                else:
                    break
            dp[i] = best
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
        




        