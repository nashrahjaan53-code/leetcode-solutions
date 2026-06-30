class Solution:
    def restoreIpAddresses(self, s):
        result = []
        
        def backtrack(start, segments):
            # Base case: we have 4 segments and used all characters
            if len(segments) == 4:
                if start == len(s):
                    result.append('.'.join(segments))
                return
            
            # Pruning: if remaining characters can't form required segments
            remaining = 4 - len(segments)
            if start + remaining > len(s) or start + 3 * remaining < len(s):
                return
            
            # Try to take 1, 2, or 3 digits for the current segment
            for i in range(1, 4):
                if start + i > len(s):
                    break
                
                segment = s[start:start + i]
                
                # Check if segment is valid
                # 1. No leading zeros unless segment is "0"
                if len(segment) > 1 and segment[0] == '0':
                    break  # Break because longer segments will also have leading zeros
                
                # 2. Value must be between 0 and 255
                if int(segment) > 255:
                    break  # Break because longer segments will be even larger
                
                # Recurse
                segments.append(segment)
                backtrack(start + i, segments)
                segments.pop()
        
        backtrack(0, [])
        return result






        