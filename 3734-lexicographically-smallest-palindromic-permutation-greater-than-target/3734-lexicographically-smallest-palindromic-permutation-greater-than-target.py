class Solution:
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        odd_count = sum(1 for f in freq if f % 2 == 1)
        if odd_count > 1:
            return ""
        
        mid_char = ''
        if n % 2 == 1:
            for i in range(26):
                if freq[i] % 2 == 1:
                    mid_char = chr(ord('a') + i)
                    freq[i] -= 1
                    break
        
        half_freq = [f // 2 for f in freq]
        m = n // 2
        
        ans = None
        
        for i in range(m + 1):
            rem = half_freq[:]
            valid = True
            first_half = []
            
            for j in range(min(i, m)):
                idx = ord(target[j]) - ord('a')
                if rem[idx] == 0:
                    valid = False
                    break
                rem[idx] -= 1
                first_half.append(target[j])
            
            if not valid:
                continue
            
            if i < m:
                # Need a strictly larger character at position i
                found = False
                start = ord(target[i]) - ord('a') + 1
                for d in range(start, 26):
                    if rem[d] > 0:
                        rem[d] -= 1
                        first_half.append(chr(ord('a') + d))
                        found = True
                        break
                if not found:
                    continue
                
                # Fill remaining positions of the first half with smallest available
                for d in range(26):
                    first_half.extend([chr(ord('a') + d)] * rem[d])
            else:
                # Matched the entire first half. Fill nothing more for the half.
                # Just use the remaining (should be zero if we matched correctly, but we already decremented)
                pass
            
            # Build the full candidate
            left = ''.join(first_half)
            if len(left) != m:
                continue   # safety
            
            if n % 2 == 1:
                full = left + mid_char + left[::-1]
            else:
                full = left + left[::-1]
            
            if full > target:
                if ans is None or full < ans:
                    ans = full
        
        return ans if ans is not None else ""






        