class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum  > 9 * num or sum < 1:
            return  ""
        res = ['0'] * num
        remaining = sum
        for i in range(num):
            digit = min(9, remaining)
            res[i] = str(digit)
            remaining -= digit
            if remaining == 0:
                break
        
        return "".join(res)
        