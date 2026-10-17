class Solution:
    def countSubstrings(self, s: str) -> int:
        curr = 0
        n = len(s)
        def pali(x):
            if x == x[::-1]:
                return True
            return False
        def f(i):
            nonlocal curr
            for j in range(i, n):
                x = s[i:j+1]
                if pali(x):
                    curr += 1
                f_next(j + 1)
        def f_next(i):
            return
        for i in range(n):
            for j in range(i, n):
                if pali(s[i:j+1]):
                    curr += 1
        return curr