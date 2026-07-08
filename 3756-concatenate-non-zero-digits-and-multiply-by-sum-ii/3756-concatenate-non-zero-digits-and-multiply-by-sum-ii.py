class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)
        

        non_zero_positions = []
        non_zero_digits = []
        
        for i, ch in enumerate(s):
            if ch != '0':
                non_zero_positions.append(i)
                non_zero_digits.append(int(ch))
        
        m = len(non_zero_digits)
        

        if m == 0:
            return [0] * len(queries)
        

        prefix_sum = [0] * (m + 1)
        for i in range(m):
            prefix_sum[i+1] = (prefix_sum[i] + non_zero_digits[i]) % MOD
        

        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
        


        suffix_val = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            suffix_val[i] = (non_zero_digits[i] * pow10[m - 1 - i] + suffix_val[i+1]) % MOD
        

        prefix_val = [0] * (m + 1)
        for i in range(m):
            prefix_val[i+1] = (prefix_val[i] * 10 + non_zero_digits[i]) % MOD
        
        result = []
        for l, r in queries:

            import bisect
            left_idx = bisect.bisect_left(non_zero_positions, l)
            right_idx = bisect.bisect_right(non_zero_positions, r) - 1
            
            if left_idx > right_idx:
                result.append(0)
                continue
            
            cnt = right_idx - left_idx + 1
            digit_sum = (prefix_sum[right_idx + 1] - prefix_sum[left_idx]) % MOD
            


            x = prefix_val[right_idx + 1]
            if left_idx > 0:
  
                x = (x - (prefix_val[left_idx] * pow10[cnt]) % MOD + MOD) % MOD
            
            result.append((x * digit_sum) % MOD)
        
        return result






        