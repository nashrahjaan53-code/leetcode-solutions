class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        
        total_gas = 0
        total_cost = 0
        tank = 0
        start = 0
        
        for i in range(n):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            


            if tank < 0:
                start = i + 1
                tank = 0
        

        if total_gas < total_cost:
            return -1
        
        return start






        