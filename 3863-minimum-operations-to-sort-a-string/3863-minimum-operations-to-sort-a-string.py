class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 1:
            return 0
        if all(s[i] <= s[i+1] for i in range(n-1)):
            return 0
        if n == 2:
            return -1
        mn = min(s)
        mx = max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        has_mn_prefix = any(s[i] == mn for i in range(n-1))
        has_mx_suffix = any(s[i] == mx for i in range(1, n))
        
        if has_mn_prefix or has_mx_suffix:
            return 2
        return 3   