class Solution:
    def minWindow(self, s,t):
        if not s or not t:
            return ""
        
        from collections import Counter
        
        need = Counter(t)
        window = {}
        have = 0
        need_count = len(need)
        
        left = 0
        min_len = float('inf')
        min_start = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                have += 1
            
            while have == need_count:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                left += 1
        
        return s[min_start:min_start + min_len] if min_len != float('inf') else ""






        