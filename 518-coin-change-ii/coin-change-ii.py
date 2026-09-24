class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1)for i in range(n)]
        def f(i,amount):
            if amount==0:
                return 1
            if i<0:
                return 0
            if dp[i][amount]!=-1:
                return dp[i][amount]
            skip = 0
            take = 0
            if coins[i]<=amount:
                take = f(i,amount-coins[i])
            skip = f(i-1,amount)
            dp[i][amount] = take+skip
            return dp[i][amount]
        return f(n-1,amount)
        