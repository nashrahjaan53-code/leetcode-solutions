class Solution:
    def isPalindrome(self, x):
        if x < 0: 
            return False
        if x < 10:
            return True
        original = x
        reversed_num = 0

        while x > 0:
            digit =x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10
        return original == reversed_num

   



        