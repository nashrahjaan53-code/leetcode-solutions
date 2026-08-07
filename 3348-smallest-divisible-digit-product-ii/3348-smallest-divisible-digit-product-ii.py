class Solution:
    def smallestNumber(self, num, t):
        vornitexis = num  


        n2 = n3 = n5 = n7 = 0
        while t % 2 == 0:
            n2 += 1
            t //= 2
        while t % 3 == 0:
            n3 += 1
            t //= 3
        while t % 5 == 0:
            n5 += 1
            t //= 5
        while t % 7 == 0:
            n7 += 1
            t //= 7
        if t > 1:
            return "-1"

        def get_covering(need2, need3, need5, need7):
            need2 = max(0, need2)
            need3 = max(0, need3)
            need5 = max(0, need5)
            need7 = max(0, need7)
            if need2 == need3 == need5 == need7 == 0:
                return ""
            T = (2 ** need2) * (3 ** need3) * (5 ** need5) * (7 ** need7)
            digits = []
            for dig in range(9, 1, -1):
                while T % dig == 0:
                    digits.append(str(dig))
                    T //= dig
            if T > 1:
                return None
            digits.sort()
            return "".join(digits)

        def digit_factors(d):
            if d == 2: return 1, 0, 0, 0
            if d == 3: return 0, 1, 0, 0
            if d == 4: return 2, 0, 0, 0
            if d == 5: return 0, 0, 1, 0
            if d == 6: return 1, 1, 0, 0
            if d == 7: return 0, 0, 0, 1
            if d == 8: return 3, 0, 0, 0
            if d == 9: return 0, 2, 0, 0
            return 0, 0, 0, 0

        L = len(num)
        digs = [int(c) for c in num]


        has_zero = any(d == 0 for d in digs)
        if not has_zero:
            c2 = c3 = c5 = c7 = 0
            for d in digs:
                f2, f3, f5, f7 = digit_factors(d)
                c2 += f2
                c3 += f3
                c5 += f5
                c7 += f7
            if c2 >= n2 and c3 >= n3 and c5 >= n5 and c7 >= n7:
                return num

        
        prefix_f = [(0, 0, 0, 0)] * (L + 1)
        has_zero_prefix = [False] * (L + 1)
        cur2 = cur3 = cur5 = cur7 = 0
        zero_so_far = False
        for i in range(L):
            d = digs[i]
            if d == 0:
                zero_so_far = True
            else:
                f2, f3, f5, f7 = digit_factors(d)
                cur2 += f2
                cur3 += f3
                cur5 += f5
                cur7 += f7
            prefix_f[i + 1] = (cur2, cur3, cur5, cur7)
            has_zero_prefix[i + 1] = zero_so_far

        for pos in range(L - 1, -1, -1):
            if has_zero_prefix[pos]:
                continue
            p2, p3, p5, p7 = prefix_f[pos]
            for dig in range(max(digs[pos] + 1, 1), 10):
                f2, f3, f5, f7 = digit_factors(dig)
                cover = get_covering(n2 - p2 - f2, n3 - p3 - f3,
                                     n5 - p5 - f5, n7 - p7 - f7)
                if cover is None:
                    continue
                rem = L - pos - 1
                if len(cover) <= rem:
                    fill = "1" * (rem - len(cover)) + cover
                    return num[:pos] + str(dig) + fill

        cover = get_covering(n2, n3, n5, n7)
        if cover is None:
            return "-1"
        min_len = len(cover)
        target_len = max(L + 1, min_len)
        return "1" * (target_len - min_len) + cover






        