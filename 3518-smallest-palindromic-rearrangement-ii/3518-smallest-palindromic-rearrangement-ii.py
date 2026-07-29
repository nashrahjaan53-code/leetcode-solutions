class Solution:
    def smallestPalindrome(self, s, k):
        n = len(s)
        freq=[0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        middle = ''
        half = [0] * 26
        for i in range(26):
            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))
            half[i] = freq[i] // 2
        m = n // 2
        def count_perms(counts, limit):
            total = sum(counts)
            res = 1
            for f in counts:
                if f == 0: 
                    continue
                take = min(f, total - f)
                for i in range(take):
                    res *= (total - i)
                    res //= (i + 1)
                    if res > limit:
                        return limit + 1
                total -= f
            return res
        first = []
        remaining = half[:]
        for _ in range(m):
            chosen = False
            for c in range(26):
                if remaining[c] == 0:
                    continue
                remaining[c] -= 1
                ways = count_perms(remaining, k)
                if ways >= k:
                    first.append(chr(ord('a') + c))
                    chosen = True
                    break
                else:
                    k -= ways
                    remaining[c] += 1  # backtrack
            if not chosen:
                return "" 
        first_half = ''.join(first)
        if middle:
            return first_half + middle + first_half[::-1]
        return first_half + first_half[::-1]















        