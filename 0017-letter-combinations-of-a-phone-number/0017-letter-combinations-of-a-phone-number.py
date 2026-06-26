class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = [""]

        for digit in digits:
            new_result = []
            letters = phone_map[digit]

            for combination in result:
                for letter in letters:
                    new_result.append(combination +  letter)

            result = new_result
        return result
        
        

            
       


      
        