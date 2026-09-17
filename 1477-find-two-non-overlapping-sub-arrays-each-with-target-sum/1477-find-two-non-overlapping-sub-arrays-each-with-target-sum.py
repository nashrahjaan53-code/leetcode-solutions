class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = float('inf')
        best = [INF] * n
        prefix = {0: -1}
        curr = 0
        min_len = INF
        ans = INF
        for i in range(n):
            curr += arr[i]
            if curr - target in prefix:
                j = prefix[curr - target]
                length = i - j
                if j >= 0:
                    ans = min(ans, best[j] + length)
                min_len = min(min_len, length)
            best[i] = min_len
            prefix[curr] = i
        return ans if ans != INF else -1