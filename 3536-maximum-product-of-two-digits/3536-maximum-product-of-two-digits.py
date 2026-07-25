class Solution:
    def maxProduct(self, n):
        largest = second_largest = -1
        temp = n
        while temp > 0:
            digit = temp % 10
            if digit > largest:
                second_largest = largest
                largest = digit
            elif digit > second_largest:
                second_largest = digit
            temp //= 10
        return largest * second_largest




