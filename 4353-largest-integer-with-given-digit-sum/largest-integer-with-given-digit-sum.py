class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if n * 9 < s:
            return -1
        ans = 0
        while s > 0:
            x = min(s, 9)
            ans = ans * 10 + x
            s -= x
        ans = int(str(ans) + "0" * (n - len(str(ans))))
        return ans        