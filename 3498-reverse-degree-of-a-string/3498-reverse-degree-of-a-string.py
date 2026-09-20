class Solution:
    def reverseDegree(self, s):
        total = 0
        for i, c in enumerate(s):
            rev_pos = 26 - (ord(c) -ord('a'))
            str_pos = i + 1
            total += rev_pos * str_pos
        return total
        