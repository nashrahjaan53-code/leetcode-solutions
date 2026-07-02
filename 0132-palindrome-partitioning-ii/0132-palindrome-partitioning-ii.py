class Solution:
    def minCut(self, s):
        n = len(s)
        

        dp = [i for i in range(n)]
        

        for center in range(n):

            left, right = center, center
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left-1] + 1)
                left -= 1
                right += 1
            

            left, right = center, center + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    dp[right] = 0
                else:
                    dp[right] = min(dp[right], dp[left-1] + 1)
                left -= 1
                right += 1
        
        return dp[-1]





        