class Solution:
    def maximumSaleItems(self, items, budget):
        f = [0] * (budget + 1)
        mn = float('inf')
        for factor, price in items:
            mn = min(mn, price)
            cnt = sum(1 for fj, _ in items if fj % factor == 0)
            for j in range(budget, price - 1, -1):
                f[j] = max(f[j], f[j - price] + cnt)
        ans = 0
        for i in range(budget + 1):
            ans = max(ans, f[i] + (budget - i) // mn)
        return ans






        