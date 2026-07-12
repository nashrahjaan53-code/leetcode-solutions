class Solution:
    def longestBalanced(self, s):
        n = len(s)
        max_len = 0
        

        curr_len = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1
        max_len = max(max_len, curr_len)
        

        for c1, c2 in [('a', 'b'), ('a', 'c'), ('b', 'c')]:
            diff_map = {0: -1}
            cnt1 = cnt2 = 0
            
            for i, ch in enumerate(s):
                if ch == c1:
                    cnt1 += 1
                elif ch == c2:
                    cnt2 += 1
                else:
                    cnt1 = cnt2 = 0
                    diff_map = {0: i}
                    continue
                
                diff = cnt1 - cnt2
                if diff in diff_map:
                    max_len = max(max_len, i - diff_map[diff])
                else:
                    diff_map[diff] = i
        

        state_map = {(0, 0): -1}
        ca = cb = cc = 0
        
        for i, ch in enumerate(s):
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:
                cc += 1
            
            state = (ca - cb, ca - cc)
            if state in state_map:
                max_len = max(max_len, i - state_map[state])
            else:
                state_map[state] = i
        
        return max_len





        