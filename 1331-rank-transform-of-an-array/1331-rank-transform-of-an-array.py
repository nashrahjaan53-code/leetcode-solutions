class Solution:
    def arrayRankTransform(self, arr):
        rank = {val: i + 1 for i, val in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]




        