class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        arr = [1,2,3,4,5,6,7,8,9]
        ans = []
        curr = []
        def f(i, k, n):
            if k == 0:
                if n == 0:
                    ans.append(curr.copy())
                return

            if i == 9:
                return

            if arr[i] <= n:
                curr.append(arr[i])
                f(i + 1, k - 1, n - arr[i])
                curr.pop()

            f(i + 1, k, n)

        f(0, k, n)
        return ans
        