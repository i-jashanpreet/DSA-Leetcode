class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        t = 0
        i = 0
        while i < len(costs) and t + costs[i] <= coins:
            t += costs[i]
            i += 1
        return i
            
        