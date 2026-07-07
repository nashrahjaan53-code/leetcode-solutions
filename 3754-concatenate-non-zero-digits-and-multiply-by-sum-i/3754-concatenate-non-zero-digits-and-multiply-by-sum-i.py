class Solution:
    def sumAndMultiply(self, n):
        s = str(n).replace('0', '')
        return 0 if not s else int(s) * sum(int(d)for d in s)




        