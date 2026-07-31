class Solution(object):
    def minimumPushes(self, word):
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        counts = []
        for count in freq:
            if count > 0:
                counts.append(count)
        counts.sort(reverse=True)
        total_pushes = 0
        for i, count in enumerate(counts):
            cost = (i// 8) + 1
            total_pushes += count * cost
        return total_pushes
        """
        :type word: str
        :rtype: int
        """
        