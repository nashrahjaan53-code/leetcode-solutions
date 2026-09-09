class Solution:
    def countCommas(self, n):
        if n < 1000:
            return 0
        def count_up_to(x):
            if x < 1000:
                return 0
            s = str(x)
            d = len(s)
            total = 0
            for length in range(4,d):
                count = 9 * 10 **(length - 1)
                commas_per = (length - 1) // 3
                total +=  count * commas_per
            start = 10**(d - 1)
            count = x - start + 1
            commas_per = (d - 1) // 3
            total += count * commas_per
            return total
        return count_up_to(n)





       