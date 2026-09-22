class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        def f(i):
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            take = nums[i]+f(i-2)
            skip = f(i-1)
            dp[i] = max(take,skip)
            return dp[i]
        return f(n-1)
        