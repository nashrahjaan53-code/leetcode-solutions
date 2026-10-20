class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        s = sorted(nums)
        
        divs = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divs.add(i)
                divs.add(n // i)
        
        def is_rotation(block, target):
            m = len(block)
            if m == 0:
                return True
            # Use string with separator to check substring
            sep = ','
            b_str = sep.join(map(str, block))
            t_str = sep.join(map(str, target))
            doubled = b_str + sep + b_str
            return t_str in doubled
        
        ans = 0
        for k in divs:
            good = True
            for start in range(0, n, k):
                block = nums[start:start + k]
                target = s[start:start + k]
                if not is_rotation(block, target):
                    good = False
                    break
            if good:
                ans += k
        return ans





        