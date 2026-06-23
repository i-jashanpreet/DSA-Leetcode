class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        m = r - l + 1
        if n == 1:
            return m % mod
        up = [0] * (m + 1)
        down = [0] * (m + 1)
        for v in range(1, m + 1):
            up[v] = v - 1
            down[v] = m - v
        for _ in range(3, n + 1):
            newUp = [0] * (m + 1)
            newDown = [0] * (m + 1)
            pref = 0
            for v in range(1, m + 1):
                newUp[v] = pref
                pref = (pref + down[v]) % mod
            suff = 0
            for v in range(m, 0, -1):
                newDown[v] = suff
                suff = (suff + up[v]) % mod
            up = newUp
            down = newDown
        ans = 0
        for v in range(1, m + 1):
            ans = (ans + up[v] + down[v]) % mod
        return ans
        