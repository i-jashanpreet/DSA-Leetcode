class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {'a': 0, 'b': 0, 'c': 0}
        l = 0
        ans = 0
        for r in range(len(s)):
            d[s[r]] += 1
            while d["a"] and d["b"] and d["c"]:
                ans += len(s) - r
                d[s[l]] -= 1
                l += 1
        return ans


            

        