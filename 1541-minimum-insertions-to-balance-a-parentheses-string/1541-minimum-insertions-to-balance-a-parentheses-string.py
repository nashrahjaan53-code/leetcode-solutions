class Solution:
    def minInsertions(self, s):
        ans = 0
        bal = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                bal += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    ans += 1
                    i += 1
                if bal > 0:
                    bal -= 1
                else:
                    ans += 1
        ans += bal * 2
        return ans