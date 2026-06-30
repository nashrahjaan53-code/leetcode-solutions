class Solution:
    def isInterleave(self, s1, s2, s3):
        m, n, l = len(s1), len(s2), len(s3)
        
        if m + n != l:
            return False
        

        dp = [False] * (n + 1)
        dp[0] = True
        

        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        

        for i in range(1, m + 1):

            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            
            for j in range(1, n + 1):

                if s1[i-1] == s3[i+j-1]:
                    dp[j] = dp[j]
                else:
                    dp[j] = False
                

                if s2[j-1] == s3[i+j-1]:
                    dp[j] = dp[j] or dp[j-1]
        
        return dp[n]







        