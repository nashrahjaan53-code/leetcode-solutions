class Solution:
    def sequentialDigits(self, low, high):
        result = []
        

        for start in range(1, 10):
            num = start
            next_digit = start
            

            while num <= high and next_digit < 10:
                if num >= low:
                    result.append(num)
                next_digit += 1
                num = num * 10 + next_digit
        
        return sorted(result)






        