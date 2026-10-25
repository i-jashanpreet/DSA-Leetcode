class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        curr = []
        def f(i):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            for j in range(i, n + 1):
                curr.append(j)
                f(j + 1)
                curr.pop()
        f(1)
        return ans


