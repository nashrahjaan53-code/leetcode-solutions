class Solution:
    def uniqueXorTriplets(self, nums):
        if not nums:
            return 0
        S = set(nums)
        MAX = 2048

        pair_possible = [False] * MAX
        for x in S:
            for y in S:
                pair_possible[x ^ y] = True

        triple_possible = [False] * MAX
        for p in range(MAX):
            if pair_possible[p]:
                for z in S:
                    triple_possible[p ^ z] = True

        count = sum(triple_possible)
        return count






        