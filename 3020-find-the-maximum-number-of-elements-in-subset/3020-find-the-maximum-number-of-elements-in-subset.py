from collections import Counter

class Solution:
    def maximumLength(self, nums):
        cnt = Counter(nums)
        ans = 1

        
        if 1 in cnt:
            ans = cnt[1]
            if ans % 2 == 0:
                ans -= 1

        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt[cur] >= 2:
                length += 2
                cur *= cur

                if cur > 10**18:
                    break

            if cnt[cur] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans





        