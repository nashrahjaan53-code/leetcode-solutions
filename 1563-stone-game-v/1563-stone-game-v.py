class Solution:
    def stoneGameV(self, stoneValue) :
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        
        memo = [[-1] * n for _ in range(n)]
        
        def dp(i, j):
            if i >= j:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            ans = 0
            left = 0
            total = prefix[j + 1] - prefix[i]
            
            for k in range(i, j):
                left += stoneValue[k]
                right = total - left
                
                if left < right:
                    if ans >= left * 2:
                        continue
                    ans = max(ans, left + dp(i, k))
                elif left > right:
                    if ans >= right * 2:
                        break
                    ans = max(ans, right + dp(k + 1, j))
                else:
                    ans = max(ans, left + dp(i, k), right + dp(k + 1, j))
            
            memo[i][j] = ans
            return ans
        
        return dp(0, n - 1)






        