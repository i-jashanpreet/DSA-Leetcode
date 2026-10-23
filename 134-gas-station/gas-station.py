class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        n =len(gas)
        tank = 0
        ind =0
        for i in range(n):
            tank =tank+gas[i]-cost[i]
            if tank<0:
                tank = 0
                ind =i+1
        return ind
         
        