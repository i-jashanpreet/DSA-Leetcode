# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
        # p = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i-1]:
        #         p += prices[i] - prices[i-1]
        # return p

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n + 1)]
        def f(i, holding):
            if i == n:
                return 0
            if dp[i][holding] != -1:
                return dp[i][holding]
            if holding == 0:
                buy = -prices[i] + f(i + 1, 1)
                skip = f(i + 1, 0)
                profit = max(buy, skip)
            else:
                sell = prices[i] + f(i + 1, 0)
                skip = f(i + 1, 1)
                profit = max(sell, skip)
            dp[i][holding] = profit
            return profit
        return f(0, 0)