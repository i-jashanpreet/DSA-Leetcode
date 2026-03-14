class Solution:
    def numSquares(self, n: int) -> int:
        def find_ps(i):
            st = 1
            end = i
            ans = -1
            while st <= end:
                mid = (st + end) // 2

                if mid * mid == i:
                    return mid
                elif mid * mid > i:
                    end = mid - 1
                else:
                    st = mid + 1
            return ans
        ps = []
        for i in range(1, n + 1):
            if find_ps(i) != -1:
                ps.append(i)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for sq in ps:
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[n]
            
                        