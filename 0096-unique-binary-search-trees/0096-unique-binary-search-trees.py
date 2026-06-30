class Solution:
    def numTrees(self, n):
        from math import factorial
        return factorial(2 * n) // (factorial(n + 1) * factorial(n))
        



        