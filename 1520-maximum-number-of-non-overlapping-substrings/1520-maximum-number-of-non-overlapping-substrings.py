class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)
        first = [n] * 26
        last = [-1] * 26
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if first[idx] == n:
                first[idx] = i
            last[idx] = i 
        def get_right(left):
            right = last[ord(s[left]) - ord('a')]
            i = left
            while i <= right:
                cidx = ord(s[i]) - ord('a')
                if first[cidx] < left:
                    return -1
                if last[cidx] > right:
                    right = last[cidx]
                i += 1
            return right
        ans = []
        prev_right = -1
        for i in range(n):
            if i == first[ord(s[i]) - ord('a')]:
                new_right = get_right(i)
                if new_right == -1:
                    continue
                if i > prev_right:
                    ans.append(s[i: new_right + 1])
                    prev_right = new_right
                else:
                    ans[-1] = s[i:new_right + 1]
                    prev_right = new_right
        return ans