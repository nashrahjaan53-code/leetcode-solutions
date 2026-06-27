class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start, current_combination, current_sum):
            if current_sum == target:
                result.append(current_combination[:])
                return
            
            if  current_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, current_sum + candidates[i])
                current_combination.pop()

        backtrack(0, [] , 0)
        return result
                
        
        
 


        