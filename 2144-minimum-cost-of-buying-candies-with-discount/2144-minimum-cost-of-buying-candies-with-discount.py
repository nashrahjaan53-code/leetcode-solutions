class Solution(object):
    def minimumCost(self, cost):
        cost.sort()
        total = 0  
        for i in range(len(cost) - 1, -1, -1):
             if (len(cost) - 1 - i) % 3 == 2:
                continue
             total += cost[i]
        
        return total




        