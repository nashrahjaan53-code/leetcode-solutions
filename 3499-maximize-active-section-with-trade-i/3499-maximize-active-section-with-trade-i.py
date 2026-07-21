class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        n = len(s)
        if n == 0:
            return 0
        t = '1' + s + '1'
        m = len(t)
        ones = s.count('1')
        ans = ones
        i = 1
        max_zero = 0
        while i < m-1:
            if t[i] == '0':
                j = i
                while j < m-1 and t[j] == '0':
                    j += 1
                length = j - i
                max_zero = max(max_zero, length)
                if t[i-1] == '1' and t[j] == '1':
                    pass
                i = j
            else:
                i += 1
        i = 1
        while i < m - 1:
            if t[i] == '1':
                j = i
                while j < m - 1 and t[j] == '1':
                    j += 1
                length1 = j - i
                if t[i-1] == '0' and t[j] == '0': 
                     left = 0
                     p = i - 1
                     while p >= 0 and t[p] == '0':
                        left += 1
                        p -= 1
                     right = 0
                     p = j
                     while p < m and t[p] == '0':
                        right += 1
                        p += 1
                     new_merged = left + length1 + right
                     gain = new_merged - length1
                     ans = max(ans, ones + gain)
                i = j
            else:
                i += 1
        return ans






        