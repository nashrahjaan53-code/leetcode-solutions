class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        maxf = n
        freq = [0] * (maxf + 1)
        for f, _ in items:
            freq[f] += 1
        multiples = [0] * (maxf + 1)
        for f in range(1, maxf + 1):
            for m in range(f, maxf + 1, f):
                multiples[f] += freq[m]
        min_price = min(p for _, p in items)
        candidates = []
        for f, p in items:
            g = multiples[f] - 1
            if p < 2 * min_price and g > 0:
                candidates.append((p, g))
        candidates.sort()
        total = 0
        for p, g in candidates:
            can = min(g, budget // p)
            if can > 0:
                total += can * 2
                budget -= can * p
        total += budget // min_price
        return total






        