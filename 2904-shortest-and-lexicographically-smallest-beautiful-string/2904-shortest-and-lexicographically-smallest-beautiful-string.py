class Solution:
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        min_len = float('inf')
        ans =""
        for i in range(n):
            ones = 0
            for j in range(i,n):
                if s[j] == '1':
                    ones += 1
                if ones == k:
                    curr = s[i:j+1]
                    if len(curr) < min_len or (len(curr) == min_len and curr < ans):
                        min_len = len(curr)
                        ans = curr
                elif ones > k:
                    break
        return ans 
           



 

        