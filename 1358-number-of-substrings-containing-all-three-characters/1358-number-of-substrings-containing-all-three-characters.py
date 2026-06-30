class Solution(object):
    def numberOfSubstrings(self, s):
        last_pos = {'a': -1, 'b': -1, 'c': -1}
        result = 0

        for i, ch in enumerate(s):
            last_pos[ch] = i

            min_last = min(last_pos.values())
            if min_last != -1:
                result += min_last + 1
        return result




