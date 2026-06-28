class Solution(object):
    def maxSum(self, nums, k, mul):
        nums.sort(reverse=True)
        total = 0

        for i in range(k):
            if mul > 0:
                total += nums[i] * mul
                mul -= 1
            else:
                total += nums[i]
        return total
        
       
        
   

    
    
        