class Solution:
    def partition(self, s):
        result = []
        
        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backtrack(start, current_partition):
            if start == len(s):
                result.append(current_partition[:])
                return
            
            for end in range(start, len(s)):
                if is_palindrome(s, start, end):
                    current_partition.append(s[start:end+1])
                    backtrack(end + 1, current_partition)
                    current_partition.pop()
        
        backtrack(0, [])
        return result

       
      
      

        