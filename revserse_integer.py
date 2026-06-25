class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        
    
        reversed_str = str(x)[::-1]
        result = sign * int(reversed_str)
        
        # Check 32-bit overflow
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result