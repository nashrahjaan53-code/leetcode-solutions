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

            




            




            




            

            for k in range(1, length):

                if solve(i, j, k) and solve(i+k, j+k, length-k):
                    memo[key] = True
                    return True
                

                if solve(i, j+length-k, k) and solve(i+k, j, length-k):
                    memo[key] = True
                    return True
            
            memo[key] = False
            return False
        
        return solve(0, 0, len(s1))







        