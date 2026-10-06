class Solution:
    def minAddToMakeValid(self, s):
        bal = 0
        adds = 0
        for c in s:
            if c == '(':
                bal += 1
            else:
                bal -= 1
                if bal < 0 :
                    adds += 1
                    bal = 0
        return adds + bal        