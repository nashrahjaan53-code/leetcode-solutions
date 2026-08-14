class Solution(object):
    def maximumLengthSubstring(self, s):
        n = len(s)
        left = 0
        freq = [0] * 26
        max_len = 0
        for right in range(n):
            idx = ord(s[right]) - ord('a')
            freq[idx] += 1
            while freq[idx] > 2:
                freq[ord(s[left])- ord('a')] -= 1
                left += 1
            max_len =  max(max_len, right - left + 1)
        return max_len





        