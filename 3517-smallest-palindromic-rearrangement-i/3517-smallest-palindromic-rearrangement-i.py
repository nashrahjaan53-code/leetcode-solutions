class Solution:
    def smallestPalindrome(self, s):
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        result = []
        middle = ''
        for i in range(26):
            count = freq[i]
            ch = chr(i + ord('a'))
            if count % 2 == 1:
                middle = ch
            result.extend([ch] * (count // 2))
        left = ''.join(result)
        return left + middle + left[::-1]




        