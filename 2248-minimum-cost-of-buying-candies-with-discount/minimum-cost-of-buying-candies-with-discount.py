class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = 0
        i = 0
        while i < len(cost):
            ans += cost[i]
            if i + 1 < len(cost):
                ans += cost[i + 1]
            i += 3
        return ans

        