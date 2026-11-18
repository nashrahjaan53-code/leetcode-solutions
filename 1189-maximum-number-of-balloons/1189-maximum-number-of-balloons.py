class Solution:
    def maxNumberOfBalloons(self, text):
        cnt = [0] * 26
        for c in text:
            cnt[ord(c) - ord('a')] += 1
        return min(cnt[1], cnt[0], cnt[11] // 2, cnt[14] // 2, cnt[13])  # b a l o n





        