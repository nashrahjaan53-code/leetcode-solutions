class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2
        cnt1 = cnt2 = 0
        s1 = s2 = 0
        for i in range(half):
            if num[i] == '?':
                cnt1 += 1
            else:
                s1 += int(num[i])
        for i in range(half, n):
            if num[i] == '?':
                cnt2 += 1
            else:
                s2 += int(num[i])
        return (cnt1 + cnt2) % 2 == 1 or s1 - s2 != 9 * (cnt2 - cnt1) //2

        


        