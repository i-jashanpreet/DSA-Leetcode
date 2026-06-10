import heapq
from typing import List
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        K = lg[n] + 1

        st_max = [[0] * n for _ in range(K)]
        st_min = [[0] * n for _ in range(K)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            for i in range(n - length + 1):
                st_max[j][i] = max(
                    st_max[j - 1][i],
                    st_max[j - 1][i + half]
                )

                st_min[j][i] = min(
                    st_min[j - 1][i],
                    st_min[j - 1][i + half]
                )

            j += 1

        def query_max(l, r):
            j = lg[r - l + 1]
            return max(
                st_max[j][l],
                st_max[j][r - (1 << j) + 1]
            )

        def query_min(l, r):
            j = lg[r - l + 1]
            return min(
                st_min[j][l],
                st_min[j][r - (1 << j) + 1]
            )

        def value(l, r):
            return query_max(l, r) - query_min(l, r)
        heap = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)

            ans += -neg_v

            if r - 1 >= l:
                nv = value(l, r - 1)
                heapq.heappush(heap, (-nv, l, r - 1))

        return ans

        