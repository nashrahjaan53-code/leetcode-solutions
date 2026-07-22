from bisect import bisect_right

class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        total_ones = s.count('1')


        blocks = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks.append((i, j - 1, s[i]))
            i = j

        m = len(blocks)
        block_start = [b[0] for b in blocks]

        NEG = float('-inf')


        left_zero_len = [0] * m
        right_zero_len = [0] * m
        for idx in range(m):
            if blocks[idx][2] == '1':
                if idx - 1 >= 0:
                    left_zero_len[idx] = blocks[idx-1][1] - blocks[idx-1][0] + 1
                if idx + 1 < m:  
                    right_zero_len[idx] = blocks[idx+1][1] - blocks[idx+1][0] + 1

        gain_full = [ (left_zero_len[idx] + right_zero_len[idx]) if blocks[idx][2] == '1' else NEG
                      for idx in range(m) ]


        sparse = [gain_full[:]]
        k = 1
        while (1 << k) <= max(m, 1):
            prev = sparse[-1]
            length = m - (1 << k) + 1
            if length <= 0:
                break
            half = 1 << (k - 1)
            cur = [max(prev[a], prev[a + half]) for a in range(length)]
            sparse.append(cur)
            k += 1

        def range_max(a, b):
            if a > b or a < 0 or b >= m:
                return NEG
            k = (b - a + 1).bit_length() - 1
            return max(sparse[k][a], sparse[k][b - (1 << k) + 1])

        def block_index_at(pos):
            return bisect_right(block_start, pos) - 1

        def candidate_gain(j, l, r, bi_l, bi_r):
            if blocks[j][2] != '1':
                return NEG
 
            if j - 1 == bi_l:
                lst, len_, _ = blocks[j - 1]
                cl, cr = max(lst, l), min(len_, r)
                left_len = cr - cl + 1 if cl <= cr else 0
            else:
                left_len = left_zero_len[j]
  
            if j + 1 == bi_r:
                rst, ren, _ = blocks[j + 1]
                cl, cr = max(rst, l), min(ren, r)
                right_len = cr - cl + 1 if cl <= cr else 0
            else:
                right_len = right_zero_len[j]
            return left_len + right_len

        ans = []
        for l, r in queries:
            bi_l = block_index_at(l)
            bi_r = block_index_at(r)

            best_gain = 0
            if bi_r - bi_l >= 2:
                j1 = bi_l + 1
                g1 = candidate_gain(j1, l, r, bi_l, bi_r)
                if g1 != NEG:
                    best_gain = max(best_gain, g1)

                j2 = bi_r - 1
                if j2 != j1:
                    g2 = candidate_gain(j2, l, r, bi_l, bi_r)
                    if g2 != NEG:
                        best_gain = max(best_gain, g2)

                if bi_l + 2 <= bi_r - 2:
                    mid = range_max(bi_l + 2, bi_r - 2)
                    if mid != NEG:
                        best_gain = max(best_gain, mid)

            ans.append(total_ones + best_gain)

        return ans
 





        