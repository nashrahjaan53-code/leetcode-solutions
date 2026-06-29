class Solution:
    def isScramble(self, s1, s2):
        memo = {}
        
        def solve(i, j, length):
            key = (i, j, length)
            if key in memo:
                return memo[key]
            if length == 1:
                memo[key] = (s1[i] == s2[j])
                return memo[key]
            if sorted(s1[i: i +length]) != sorted(s2[j:j + length]):
                memo[key] = False
                return False

            




            




            




            
            # Try all possible split positions
            for k in range(1, length):
                # Case 1: No swap - substrings maintain order
                if solve(i, j, k) and solve(i+k, j+k, length-k):
                    memo[key] = True
                    return True
                
                # Case 2: Swap - substrings are swapped
                if solve(i, j+length-k, k) and solve(i+k, j, length-k):
                    memo[key] = True
                    return True
            
            memo[key] = False
            return False
        
        return solve(0, 0, len(s1))







        