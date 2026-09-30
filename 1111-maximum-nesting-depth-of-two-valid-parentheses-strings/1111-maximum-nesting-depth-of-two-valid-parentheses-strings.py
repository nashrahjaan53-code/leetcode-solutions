class Solution:
    def maxDepthAfterSplit(self, seq):
        ans = [0] * len(seq)
        depth = 0
        for i, c in enumerate(seq):
            if c == '(':
                ans[i] = depth % 2
                depth += 1
            else:
                depth -= 1
                ans[i] = depth % 2
        return ans