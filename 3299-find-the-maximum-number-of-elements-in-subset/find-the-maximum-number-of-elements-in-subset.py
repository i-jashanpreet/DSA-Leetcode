class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d = {}

        for x in nums:
            d[x] = d.get(x, 0) + 1

        ans = 1

        for x in d:

            if x == 1:
                if d[x] % 2:
                    ans = max(ans, d[x])
                else:
                    ans = max(ans, d[x] - 1)

                continue

            cur = x
            cnt = 0

            while d.get(cur, 0) >= 2:
                cnt += 2
                cur = cur * cur

            if d.get(cur, 0) == 1:
                cnt += 1
            else:
                cnt -= 1

            ans = max(ans, cnt)

        return ans
        