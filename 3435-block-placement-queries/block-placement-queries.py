from typing import List
from sortedcontainers import SortedList
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = max(q[1] for q in queries)
        class SegmentTree:
            def __init__(self, n):
                self.n = n
                self.tree = [0] * (4 * (n + 1))
            def update(self, idx, val, node, l, r):
                if l == r:
                    self.tree[node] = val
                    return
                mid = (l + r) // 2
                if idx <= mid:
                    self.update(idx, val, node * 2, l, mid)
                else:
                    self.update(idx, val, node * 2 + 1, mid + 1, r)
                self.tree[node] = max(
                    self.tree[node * 2],
                    self.tree[node * 2 + 1]
                )
            def query(self, ql, qr, node, l, r):
                if ql > r or qr < l:
                    return 0
                if ql <= l and r <= qr:
                    return self.tree[node]
                mid = (l + r) // 2
                return max(
                    self.query(ql, qr, node * 2, l, mid),
                    self.query(ql, qr, node * 2 + 1, mid + 1, r)
                )
        obstacles = SortedList([0])
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])
        seg = SegmentTree(max_x + 1)
        for i in range(1, len(obstacles)):
            p = obstacles[i]
            seg.update(
                p,
                p - obstacles[i - 1],
                1,
                0,
                max_x
            )
        ans = []
        for q in reversed(queries):
            if q[0] == 2:
                _, x, sz = q
                idx = obstacles.bisect_right(x) - 1
                pre = obstacles[idx]
                best_gap = seg.query(0, pre, 1, 0, max_x)
                best_gap = max(best_gap, x - pre)
                ans.append(best_gap >= sz)
            else:
                _, x = q
                idx = obstacles.index(x)
                prev_ob = obstacles[idx - 1]
                if idx + 1 < len(obstacles):
                    next_ob = obstacles[idx + 1]
                    seg.update(
                        next_ob,
                        next_ob - prev_ob,
                        1,
                        0,
                        max_x
                    )
                seg.update(x, 0, 1, 0, max_x)
                obstacles.remove(x)
        return ans[::-1]
        