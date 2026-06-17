class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n):
            ch = s[i]
            if ch.islower():
                dp[i + 1] = dp[i] + 1
            elif ch == "*":
                dp[i + 1] = max(0, dp[i] - 1)
            elif ch == "#":
                dp[i + 1] = dp[i] * 2
            else: 
                dp[i + 1] = dp[i]
        if k >= dp[n]:
            return '.'
        for i in range(n - 1, -1, -1):
            ch = s[i]
            cur = dp[i + 1]
            prev = dp[i]
            if ch.islower():
                if k == prev:
                    return ch
            elif ch == "*":
                pass
            elif ch == "#":
                k %= prev
            else:  
                k = prev - 1 - k
        return '.'
        