import re
class Solution:
    def myAtoi(self, s):
        s =s.lstrip()
        match = re.match(r'^[+-]?\d+', s)

        if not match:
            return 0
        result = int(match.group())
        
        
        
  





        







        if result < -2**31:
            return -2**31
        if result >  2**31 - 1:
            return 2 **31 - 1
        return result
        





        