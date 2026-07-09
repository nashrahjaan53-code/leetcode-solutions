class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        component = [0] * n
        comp_id = 0
        for i in range(n):
            if i > 0 and nums[i] - nums[i - 1] > maxDiff:
                comp_id += 1
            component[i] = comp_id
        result = []
        for u, v in queries:
            result.append(component[u] == component[v])
        return result







        