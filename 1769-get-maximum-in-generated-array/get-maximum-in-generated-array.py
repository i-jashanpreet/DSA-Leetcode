class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def solve(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if memo[i] != -1:
                return memo[i]
            if i % 2 == 0:
                memo[i] = solve(i // 2)
            else:
                memo[i] = solve(i // 2) + solve(i // 2 + 1)
            return memo[i]
        maxi = 0
        for i in range(n + 1):
            maxi = max(maxi, solve(i))
        return maxi     