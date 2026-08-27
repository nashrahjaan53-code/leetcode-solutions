class Solution:
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        ans = None
        
        for i in range(n):
            rem = freq[:]
            valid = True
            prefix = []
            
            for j in range(i):
                idx = ord(target[j]) - ord('a')
                if rem[idx] == 0:
                    valid = False
                    break
                rem[idx] -= 1
                prefix.append(target[j])
            
            if not valid:
                continue
            

            found = False
            start = ord(target[i]) - ord('a') + 1
            for d in range(start, 26):
                if rem[d] > 0:
                    rem[d] -= 1
                    prefix.append(chr(ord('a') + d))
                    found = True
                    break
            
            if not found:
                continue
           

            rest = []
            for d in range(26):
                rest.extend([chr(ord('a') + d)] * rem[d])
            
            candidate = ''.join(prefix) + ''.join(rest)
            if ans is None or candidate < ans:
                ans = candidate
        
        return ans if ans is not None else ""



   


        