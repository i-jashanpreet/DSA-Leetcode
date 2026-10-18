class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        memo = {}
        def f(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if target in memo:
                return memo[target]
            ways = 0
            for num in nums:
                ways += f(target - num)
            memo[target] = ways
            return ways
        return f(target)
        