class Solution:
    def smallestNumber(self, n, t):
        def digit_product(num):
            product = 1
            for digit in str(num):
                product *= int(digit)
            return product
        num = n
        while True:
            if digit_product(num) % t == 0:
                return num
            num += 1





        